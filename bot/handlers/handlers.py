import asyncio
import logging
import os
import re
from datetime import datetime, timedelta
from functools import wraps
from typing import Optional, Union

from aiogram import F, Router, types
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import Command, CommandObject
from aiogram.types import FSInputFile

from bot.database.database import Database, UserManager
from bot.database.models import User
from bot.keyboards.keyboards import get_models_keyboard
from bot.locales.utils import get_text
from bot.services.gpt import GPTService
from bot.services.claude import ClaudeService
from config import (
    DAILY_TOKENS,
    GPT_MODEL,
    CLAUDE_MODEL,
    MODEL_NAMES,
    REFERRAL_TOKENS,
    REQUIRED_CHANNELS,
    YOUR_ADMIN_ID,
)

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODEL_SERVICES = {
    GPT_MODEL: GPTService(),
    CLAUDE_MODEL: ClaudeService(),
}


router = Router()


def escape_markdown(text):
    """Экранирует специальные символы MarkdownV2"""
    chars = [
        "_",
        "*",
        "[",
        "]",
        "(",
        ")",
        "~",
        "`",
        ">",
        "#",
        "+",
        "-",
        "=",
        "|",
        "{",
        "}",
        ".",
        "!",
    ]
    for char in chars:
        text = text.replace(char, f"\\{char}")
    return text


def format_to_html(text):
    # Заголовки
    text = re.sub(r"### \*\*(.*?)\*\*", r"<b><u>\1</u></b>", text)

    # Жирный текст
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)

    # Курсив
    text = re.sub(r"\*(.*?)\*", r"<i>\1</i>", text)

    # Разделители - заменяем на строку символов
    text = text.replace("---", "—————————")

    return text


async def check_subscription(bot, user_id: int) -> bool:
    """
    Checks if user is subscribed to all required channels.
    Returns True only if subscribed to ALL channels.
    """
    try:
        for channel in REQUIRED_CHANNELS:
            # Remove '@' from the beginning if it exists for API call
            channel_id = channel
            if channel_id.startswith('@'):
                channel_id = channel_id[1:]
                
            member = await bot.get_chat_member('@' + channel_id, user_id)
            if member.status in ["left", "kicked", "banned"]:
                # If not subscribed to any channel, return False immediately
                return False
                
        # If we get here, user is subscribed to all channels
        return True
    except Exception as e:
        logger.error(f"Subscription check failed for user {user_id}: {str(e)}")
        # Return False on any error to be safe
        return False


def require_access(func):
    @wraps(func)
    async def wrapper(message: types.Message, db: Database, *args, **kwargs):
        manager = await db.get_user_manager()
        user = await manager.get_user(
            message.from_user.id,
            message.from_user.username,
            message.from_user.language_code,
        )

        # Проверяем подписку независимо от текущего access_granted
        access_granted = await check_subscription(message.bot, user.user_id)

        if not access_granted:
            # Если не подписан, отправляем сообщение и прерываем выполнение
            # Format channels for display, e.g. "@Channel1, @Channel2"
            channels_formatted = ", ".join(REQUIRED_CHANNELS)
                
            await send_localized_message(
                message,
                "access_denied_subscription",
                user,
                channels=channels_formatted,
                reply_markup=get_subscription_keyboard(user.language_code),
            )
            # Если access_granted был True, сбрасываем его в False
            if user.access_granted:
                await manager.update_user(
                    user.user_id,
                    {
                        "access_granted": False,
                        "tariff": "free",
                    },  # Сбрасываем тариф и доступ
                )
            return

        # Если подписан, но access_granted был False, обновляем
        if not user.access_granted:
            await manager.update_user(
                user.user_id,
                {
                    "access_granted": True,
                    "tariff": "paid",
                    "last_daily_reward": datetime.now(),
                },
            )
            user.access_granted = True
            user.tariff = "paid"

        # Выполняем основную функцию
        return await func(message, db, user=user, *args, **kwargs)

    return wrapper


def get_subscription_keyboard(language_code: str) -> types.InlineKeyboardMarkup:
    """Creates a keyboard with buttons to join all required channels"""
    keyboard = []
    
    # Add a button for each channel
    for channel in REQUIRED_CHANNELS:
        # Remove '@' from the beginning if it exists for URL
        channel_id = channel
        if channel_id.startswith('@'):
            channel_id = channel_id[1:]
            
        keyboard.append([
            types.InlineKeyboardButton(
                text=f"{get_text('join_channel_button', language_code)} {channel}",
                url=f"https://t.me/{channel_id}",
            )
        ])
    
    # Add the check subscription button at the end
    keyboard.append([
        types.InlineKeyboardButton(
            text=get_text("check_subscription_button", language_code),
            callback_data="check_subscription",
        )
    ])
    
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard)


async def send_localized_message(
    message: types.Message,
    key: str,
    user: User,
    reply_markup: Optional[types.InlineKeyboardMarkup] = None,
    return_text: bool = False,
    **kwargs,
) -> Union[str, None]:
    kwargs.setdefault("username", user.username or "")
    kwargs.setdefault("invite_link", "")
    text = get_text(key, user.language_code, **kwargs)
    if return_text:
        return text
    await message.answer(text, reply_markup=reply_markup)
    return None


@router.message(Command("send_all"))
async def admin_send_all(message: types.Message, command: CommandObject, db: Database):
    if message.from_user.id != YOUR_ADMIN_ID:
        await message.answer("У вас нет прав для выполнения этой команды")
        return

    if not command.args:
        await message.answer("Использование: /send_all текст сообщения")
        return

    text = command.args
    users = await db.users.find({}).to_list(None)
    success_count = 0
    failed_count = 0

    for user in users:
        try:
            await message.bot.send_message(user["user_id"], text)
            success_count += 1
        except Exception as e:
            print(f"Ошибка отправки сообщения пользователю {user['user_id']}: {str(e)}")
            failed_count += 1

    await message.answer(
        f"Отправлено сообщений: {success_count}, не удалось отправить: {failed_count}"
    )


@router.message(Command("invite"))
@require_access
async def invite_command(message: types.Message, db: Database, user: User):
    invite_link = f"https://t.me/DockMixAIbot?start={user.user_id}"
    text = "\n\n".join(
        [
            f"🔗 Ваше реферальное посилання: {invite_link}",
            f"👥 Ви запросили: {len(user.invited_users)} користувачів",
        ]
    )
    await message.answer(text)


@router.message(Command("start"))
async def start_command(message: types.Message, db: Database):
    manager = await db.get_user_manager()
    user = await manager.get_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.language_code,
    )

    invite_link = f"https://t.me/DockMixAIbot?start={user.user_id}"
    if len(message.text.split()) > 1:
        await process_referral(message, user, db)

    # Проверяем подписку всегда
    access_granted = await check_subscription(message.bot, user.user_id)
    if access_granted and not user.access_granted:
        await manager.update_user(
            user.user_id,
            {
                "access_granted": True,
                "tariff": "paid",
                "last_daily_reward": datetime.now(),
            },
        )
        user.access_granted = True
        user.tariff = "paid"
    elif not access_granted and user.access_granted:
        await manager.update_user(
            user.user_id,
            {"access_granted": False, "tariff": "free"},
        )
        user.access_granted = False
        user.tariff = "free"

    caption_key = "start" if access_granted else "access_denied_subscription"
    
    # Format channels for display, e.g. "@Channel1, @Channel2"
    channels_formatted = ", ".join(REQUIRED_CHANNELS)
        
    caption = await send_localized_message(
        message,
        caption_key,
        user,
        channels=channels_formatted,
        invite_link=invite_link,
        balance=user.balance,
        current_model=user.current_model,
        return_text=True,
    )

    # Отправляем фото только если у пользователя нет доступа
    reply_markup = (
        None if access_granted else get_subscription_keyboard(user.language_code)
    )
    if not access_granted:
        photo = FSInputFile("image/welcome.png")
        await message.answer_photo(photo, caption=caption, reply_markup=reply_markup)
    else:
        await message.answer(caption, reply_markup=reply_markup)


@router.callback_query(F.data == "check_subscription")
async def check_subscription_callback(callback: types.CallbackQuery, db: Database):
    manager = await db.get_user_manager()
    user = await manager.get_user(
        callback.from_user.id,
        callback.from_user.username,
        callback.from_user.language_code,
    )
    access_granted = await check_subscription(callback.message.bot, user.user_id)

    if access_granted:
        await manager.update_user(
            user.user_id,
            {
                "access_granted": True,
                "tariff": "paid",
                "last_daily_reward": datetime.now(),
            },
        )
        await callback.message.edit_caption(
            caption=await send_localized_message(
                callback.message, "subscription_confirmed", user, return_text=True
            ),
            reply_markup=None,
        )
        welcome_text = await send_localized_message(
            callback.message,
            "start",
            user,
            balance=user.balance,
            current_model=user.current_model,
            return_text=True,
        )
        await callback.message.answer(welcome_text)
    else:
        # Format channels for alert message
        missing_channels = []
        for channel in REQUIRED_CHANNELS:
            try:
                channel_id = channel
                if channel_id.startswith('@'):
                    channel_id = channel_id[1:]
                    
                member = await callback.message.bot.get_chat_member('@' + channel_id, user.user_id)
                if member.status in ["left", "kicked", "banned"]:
                    missing_channels.append(channel)
            except Exception:
                missing_channels.append(channel)
                
        missing_text = ", ".join(missing_channels) if missing_channels else ", ".join(REQUIRED_CHANNELS)
            
        await callback.answer(
            get_text("still_not_subscribed", user.language_code) + f" {missing_text}", show_alert=True
        )


@router.message(Command("profile"))
@require_access
async def profile_command(message: types.Message, db: Database, user: User):
    await send_localized_message(
        message,
        "profile",
        user,
        user_id=user.user_id,
        balance=user.balance,
        current_model=user.current_model,
    )


@router.message(Command("help"))
@require_access
async def help_command(message: types.Message, db: Database, user: User):
    await send_localized_message(
        message, "help", user, balance=user.balance, current_model=user.current_model
    )


@router.message(Command("reset"))
@require_access
async def reset_command(message: types.Message, db: Database, user: User):
    manager = await db.get_user_manager()
    await manager.update_user(user.user_id, {"messages_history": []})
    await send_localized_message(message, "history_reset", user)


@router.message(Command("models"))
@require_access
async def models_command(message: types.Message, db: Database, user: User):
    await send_localized_message(
        message,
        "select_model",
        user,
        current_model=user.current_model,
        reply_markup=get_models_keyboard(user.language_code),
    )


@router.callback_query(F.data.startswith("model_"))
@require_access
async def change_model_handler(callback: types.CallbackQuery, db: Database, user: User):
    model = callback.data.split("_")[1]
    manager = await db.get_user_manager()
    await manager.update_user(user.user_id, {"current_model": model})
    await send_localized_message(
        callback.message, "model_changed", user, model=MODEL_NAMES[model]
    )








@router.message(Command("audio"))
@require_access
async def audio_command(message: types.Message, db: Database, user: User):
    try:
        text = message.text.split("/audio", 1)[1].strip()
    except IndexError:
        await send_localized_message(message, "audio_prompt_required", user)
        return

    if user.balance < 5:
        await message.answer("У вас недостатньо токенів для генерації аудіо.")
        return

    try:
        await message.bot.send_chat_action(
            chat_id=message.chat.id, action=ChatAction.RECORD_VOICE
        )

        gpt_service = MODEL_SERVICES[GPT_MODEL]
        output_path = f"audio_{message.from_user.id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"

        await gpt_service.text_to_speech(text, output_path=output_path)

        if os.path.exists(output_path):
            audio = FSInputFile(output_path)
            await message.answer_voice(audio)

            # Дожидаемся завершения отправки, потом удаляем файл
            await asyncio.sleep(1)
            os.remove(output_path)

            manager = await db.get_user_manager()
            await manager.update_balance_and_history(
                user.user_id, 5, "tts-1", text, "audio_generated"
            )
        else:
            await message.answer("Помилка: файл аудіо не був створений")
    except Exception as e:
        logger.error(f"Audio generation failed: {str(e)}")
        await message.answer(f"Помилка генерації аудіо: {str(e)}")


async def process_referral(message: types.Message, user: User, db: Database) -> None:
    if len(message.text.split()) <= 1:
        return
    try:
        inviter_id = int(message.text.split()[1])
        if inviter_id == user.user_id:
            await message.answer("❌ Ви не можете запросити самого себе!")
            return

        inviter = await db.users.find_one({"user_id": inviter_id})
        if not inviter or message.from_user.id in inviter.get("invited_users", []):
            return

        manager = await db.get_user_manager()
        await manager.add_invited_user(inviter_id, message.from_user.id)
        await send_inviter_notification(
            inviter_id, len(inviter.get("invited_users", []) + 1), db, message.bot
        )
    except (ValueError, TypeError) as e:
        logger.error(f"Помилка обробки реферала: {str(e)}")


async def send_inviter_notification(
    inviter_id: int, invited_count: int, db: Database, bot
) -> None:
    manager = await db.get_user_manager()
    user = await manager.get_user(
        inviter_id, None, "en"
    )  # Username не нужен для уведомления
    text = await send_localized_message(
        None,
        "new_invited_user_tokens",
        user,
        invited_count=invited_count,
        referral_tokens=REFERRAL_TOKENS,
        return_text=True,
    )
    await bot.send_message(inviter_id, text)


@router.message()
@require_access
async def handle_message(message: types.Message, db: Database, user: User):
    # Проверка баланса
    tokens_cost = 0 if user.current_model == "tts-1" else 1
    if user.balance < tokens_cost:
        next_day = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        await send_localized_message(message, "no_tokens", user, next_day=next_day)
        return

    # Отправляем сообщение об ожидании
    wait_message = await message.answer(
        "⏳ Ваш запит обробляється, будь ласка, зачекайте..."
    )

    try:
        await message.bot.send_chat_action(
            chat_id=message.chat.id, action=ChatAction.TYPING
        )
        service = MODEL_SERVICES.get(user.current_model)
        if not service:
            await message.bot.delete_message(message.chat.id, wait_message.message_id)
            await message.answer(
                "❌ Невідома модель, спробуйте вибрати ще раз модель /models"
            )
            return

        # Обработка сообщения
        if message.photo:
            # Обработка фото...
            photo = message.photo[-1]
            file = await message.bot.get_file(photo.file_id)
            file_path = f"temp_{message.from_user.id}_{photo.file_id}.jpg"
            await message.bot.download_file(file.file_path, file_path)
            response = await service.read_image(file_path)
            import os

            os.remove(file_path)
        else:
            # Обработка текста...
            history = user.messages_history[-5:]
            context = [
                {
                    "role": "user" if i % 2 == 0 else "assistant",
                    "content": entry["message" if i % 2 == 0 else "response"],
                }
                for i, entry in enumerate(history)
            ]
            response = await service.get_response(message.text, context=context)

        # Обновление баланса
        manager = await db.get_user_manager()
        if not message.photo:
            await manager.update_balance_and_history(
                user.user_id, tokens_cost, user.current_model, message.text, response
            )
        else:
            await manager.update_balance_and_history(
                user.user_id, tokens_cost, user.current_model, "", response
            )

        # Удаляем сообщение об ожидании
        await message.bot.delete_message(message.chat.id, wait_message.message_id)

        # Отправка ответа
        try:
            formatted_response = format_to_html(response)
            await message.answer(formatted_response, parse_mode=ParseMode.HTML)
        except Exception as e:
            await message.answer(response)
            logger.error(f"HTML format error: {str(e)}")
    except Exception as e:
        # Удаляем сообщение об ожидании при ошибке
        await message.bot.delete_message(message.chat.id, wait_message.message_id)
        logger.error(f"Message handling failed: {str(e)}")
        await message.answer(f"Помилка обробки повідомлення: {str(e)}")
