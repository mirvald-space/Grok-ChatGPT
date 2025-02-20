from datetime import datetime

from aiogram import Dispatcher, F, Router, types
from aiogram.enums import ChatAction
from aiogram.filters import Command, StateFilter

from bot.keyboards.keyboards import (
    get_models_keyboard,
    get_payment_keyboard,
    get_start_keyboard,
)
from bot.services.claude import ClaudeService
from bot.services.gpt import GPTService
from bot.services.together import TogetherService
from config import CLAUDE_MODEL, GPT_MODEL, TOGETHER_MODEL
from database import Database

gpt_service = GPTService()
claude_service = ClaudeService()
together_service = TogetherService()

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message, db: Database):
    await db.add_user(user_id=message.from_user.id, username=message.from_user.username)

    await message.answer(
        "👋 Привет! Я бот с доступом к различным AI моделям.\n"
        "💰 Ваш текущий баланс: 0 токенов\n"
        "🤖 Текущая модель: GPT\n\n"
        "Выберите действие:",
        reply_markup=get_start_keyboard(),
    )


@router.callback_query(F.data == "help")
async def help_callback(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "ℹ️ Справка по использованию бота:\n\n"
        "1. Выберите AI модель\n"
        "2. Пополните баланс\n"
        "3. Отправляйте сообщения для общения с AI\n\n"
        "Выберите действие:",
        reply_markup=get_start_keyboard(),
    )
    await callback.answer()


@router.callback_query(F.data == "select_model")
async def select_model_callback(callback: types.CallbackQuery, db: Database):
    user = await db.users.find_one({"user_id": callback.from_user.id})
    if user:
        await callback.message.edit_text(
            f"🤖 Текущая модель: {user['current_model']}\n\n" "Выберите модель:",
            reply_markup=get_models_keyboard(),
        )
    await callback.answer()


@router.callback_query(F.data.startswith("model_"))
async def change_model_handler(callback: types.CallbackQuery, db: Database):
    model = callback.data.split("_")[1]

    await db.users.update_one(
        {"user_id": callback.from_user.id}, {"$set": {"current_model": model}}
    )

    models = {GPT_MODEL: "GPT-4", CLAUDE_MODEL: "Claude 3", TOGETHER_MODEL: "Together"}

    await callback.message.edit_text(
        f"✅ Модель изменена на {models[model]}\n\n"
        "Можете отправлять сообщения\n\n"
        "Вернуться в меню:",
        reply_markup=get_start_keyboard(),
    )
    await callback.answer()


@router.callback_query(F.data == "add_balance")
async def add_balance_callback(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "💰 Выберите сумму пополнения:", reply_markup=get_payment_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == "back_to_start")
async def back_to_start_callback(callback: types.CallbackQuery, db: Database):
    user = await db.users.find_one({"user_id": callback.from_user.id})
    await callback.message.edit_text(
        f"👋 Главное меню\n"
        f"💰 Ваш текущий баланс: {user['balance']} токенов\n"
        f"🤖 Текущая модель: {user['current_model']}\n\n"
        f"Выберите действие:",
        reply_markup=get_start_keyboard(),
    )
    await callback.answer()


@router.message(StateFilter(None))
async def handle_message(message: types.Message, db: Database):
    user = await db.users.find_one({"user_id": message.from_user.id})

    if not user:
        await message.answer("❌ Вы не зарегистрированы. Используйте /start")
        return

    if user["balance"] <= 0:
        await message.answer("❌ Недостаточно токенов. Пополните баланс!")
        return

    await message.bot.send_chat_action(
        chat_id=message.chat.id, action=ChatAction.TYPING
    )

    try:
        if user["current_model"] == GPT_MODEL:
            response = await gpt_service.get_response(message.text)
        elif user["current_model"] == CLAUDE_MODEL:
            response = await claude_service.get_response(message.text)
        elif user["current_model"] == TOGETHER_MODEL:
            response = await together_service.get_response(message.text)
        else:
            await message.answer("❌ Неизвестная модель")
            return

        # Сохраняем историю и вычитаем токены только после успешного получения ответа
        await db.users.update_one(
            {"user_id": message.from_user.id},
            {
                "$inc": {"balance": -1},
                "$push": {
                    "messages_history": {
                        "model": user["current_model"],
                        "message": message.text,
                        "response": response,
                        "timestamp": datetime.utcnow(),
                    }
                },
            },
        )

        await message.answer(response)
    except Exception as e:
        await message.answer(f"❌ Произошла ошибка: {str(e)}")
        # Логирование ошибки для последующей диагностики
        print(f"Error for user {message.from_user.id}: {str(e)}")
