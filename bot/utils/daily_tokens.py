from datetime import datetime, timedelta

from config import DAILY_TOKENS


async def daily_rewards_task(bot, db):
    """Начисляет ежедневные токены всем пользователям с тарифом 'paid', сбрасывая баланс"""
    # Текущая дата, сброшенная до начала дня
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday = today - timedelta(days=1)

    # Получаем пользователей, которым нужно начислить токены
    query = {
        "tariff": "paid",
        "$or": [
            {"last_daily_reward": {"$lt": yesterday}},
            {"last_daily_reward": {"$exists": False}},
        ],
    }

    users = await db.users.find(query).to_list(length=None)

    success_count = 0
    failed_count = 0

    for user in users:
        try:
            # Сбрасываем баланс и устанавливаем DAILY_TOKENS, обновляем время
            await db.users.update_one(
                {"user_id": user["user_id"]},
                {
                    "$set": {
                        "balance": DAILY_TOKENS,  # Устанавливаем фиксированное значение
                        "last_daily_reward": datetime.now(),
                    },
                },
            )
            success_count += 1

        except Exception as e:
            print(
                f"Ошибка при начислении токенов пользователю {user['user_id']}: {str(e)}"
            )
            failed_count += 1

    print(
        f"Ежедневные токены: начислено {success_count} пользователям, не удалось {failed_count}"
    )

    return success_count, failed_count
