texts = {
    "ru": {
        "start": "👋 Привет, <b>{username}!</b>\n\nЭто бот для работы с актуальными моделями нейросетей в Telegram.\n\nКоманды:\n/start - перезапуск\n/models - выбрать нейросеть\n/profile - профиль пользователя\n/add_balance - купить подписку\n/img - генерация изображений\n/help - помощь\n\nЧтобы начьзовать нейросеть, просто напишите текст и отправьте его боту. Он будет использовать выбранную вами модель.",
        "profile": "Это ваш профиль.\n\nID: <b>{user_id}</b>\n\nБаланс: <b>{balance}</b>\n\nТекущая модель: <b>{current_model}</b>\n\nЧтобы добавить баланс нажмите /pay\n\nЛимиты: GPT-4o mini — осталось 29/30 o3-mini — осталось 10/10\n\nОбновление лимитов: пятница, 28 февраля 2025 г. в 05:27 (мск)",
        "help": "<b>О боте </b>\nБот работает через официальные API.\nМы предоставляем 10 запросов бесплатно, обновляющихся каждую неделю. Чтобы использовать бота без ограничений, вы можете приобрести подписку по команде /pay.\n\n<b>Что такое контекст?</b>\nПо умолчанию бот работает в режиме контекста, запоминая предыдущие сообщения для удобства ведения диалога в рамках одной темы. Команда /reset сбрасывает контекст.\n\n<b>Генерация изображений</b>\n- Чтобы обратиться к Midjourney или Flux, отправьте команду и текст запроса: «/img текст запроса».\n- Для генерации изображения на основе другого изображения прикрепите его к вашему запросу или вставьте ссылку на изображение.\nГенерация доступна на русском и английском языках.\n\n<i>Лимиты и подписка</i>\nЧтобы поддерживать стабильную работу без перегрузок, мы используем лимиты на генерацию. Сейчас лимиты такие:\n\nБесплатно:\n- GPT-4o mini — 30 запросов в неделю;\n- o3-mini — 10 запросов в неделю;\n\n⚡️В подписке Plus:\n- GPT-4o mini — безлимитно;\n- GPT-4o — 50 запросов в день;\n- o3-mini — 50 запросов в день;\n- GPT-4o Vision (Распознавание изображений);\n- Midjourney v6.0 — 25 запросов в день;\n- Flux.1 dev — 25 запросов в день.\n\nУправлять подпиской можно в разделе /profile.",
        "select_model": "🤖 Текущая модель: {current_model}\n\nВыберите модель:",
        "model_changed": "✅ Модель изменена на {model}\n\nМожете отправлять сообщения.\n\nВернуться в меню:",
        "add_balance": "💰 Выберите сумму пополнения:",
        "image_mode_on": "🎨 Режим генерации изображений <b>ВКЛЮЧЕН</b>\n\nОтправьте описание желаемого изображения.",
        "image_mode_off": "📝 Режим генерации изображений <b>ВЫКЛЮЧЕН</b>\n\nМожете отправлять текстовые сообщения.",
        "back_to_start": "👋 Главное меню\n💰 Ваш текущий баланс: {balance} токенов\n🤖 Текущая модель: {current_model}\n\nВыберите действие:",
        "no_tokens": "❌ Недостаточно токенов. Пополните баланс!",
        "no_image_tokens": "❌ Для генерации изображения нужно минимум 5 токенов!",
        "error": "❌ Произошла ошибка: {error}",
        "select_model_button": "🤖 Выбрать модель",
        "toggle_image_mode_on": "🎨 Вкл. режим изображений",
        "toggle_image_mode_off": "🎨 Выкл. режим изображений",
        "add_balance_button": "💰 Пополнить баланс",
        "help_button": "ℹ️ Помощь",
        "pay_50": "50 токенов - 5$",
        "pay_100": "100 токенов - 10$",
        "pay_150": "150 токенов - 15$",
        "pay_200": "200 токенов - 20$",
        "gpt_button": "GPT",
        "claude_button": "Claude",
        "free_llama_button": "🎁 FREE LLaMA",
    },
    "en": {
        "start": "👋 Hello, <b>{username}!</b>\nI am a bot with access to various AI models.\n\n"
        "💰 Your current balance: <b>{balance} tokens</b>\n"
        "🤖 Current model: <b>{current_model}</b>\n\n"
        "Generation cost: <b>1 token = 1 message</b>\n\n"
        "* To start using the neural network, just write a text and send it to the bot, it will use the model you selected.",
        "profile": "Это ваш профиль. Username: <b>{user_id}!</b> Баланс: <b>{balance}</b> Чтобы добавить баланс нажмите /pay Лимиты GPT-4o mini — осталось 29/30 o3-mini — осталось 10/10 Обновление лимитов: пятница, 28 февраля 2025 г. в 05:27 (мск)",
        "help": "ℹ️ <b>BOT USAGE GUIDE</b>\n"
        "─────────────────────────\n\n"
        "🤖 <b>Available models:</b>\n"
        "• <b>GPT-4</b> - the most powerful model, great for complex tasks\n"
        "• <b>Claude 3</b> - specializes in long dialogues and analysis\n"
        "• <b>Together</b> - fast model for simple requests\n\n"
        "💰 <b>Usage cost:</b>\n"
        "• Text request - <b>1 token</b>\n"
        "• Image generation - <b>5 tokens</b>\n\n"
        "📝 <b>How to use:</b>\n"
        "1️⃣ Select an AI model\n"
        "2️⃣ Top up your balance\n"
        "3️⃣ Send text messages or enable image generation mode\n\n"
        "⚠️ <b>IMPORTANT:</b>\n"
        "After generating an image, don't forget to turn off image mode, "
        "so you don't accidentally spend 5 tokens on the next message!\n\n"
        "─────────────────────────\n"
        "<i>Choose an action:</i>",
        "select_model": "🤖 Current model: {current_model}\n\nChoose a model:",
        "model_changed": "✅ Model changed to {model}\n\nYou can send messages\n\nReturn to menu:",
        "add_balance": "💰 Choose the top-up amount:",
        "image_mode_on": "🎨 Image generation mode <b>ENABLED</b>\n\nSend a description of the desired image",
        "image_mode_off": "📝 Image generation mode <b>DISABLED</b>\n\nYou can send text messages",
        "back_to_start": "👋 Main menu\n💰 Your current balance: {balance} tokens\n🤖 Current model: {current_model}\n\nChoose an action:",
        "no_tokens": "❌ Not enough tokens. Top up your balance!",
        "no_image_tokens": "❌ You need at least 5 tokens to generate an image!",
        "error": "❌ An error occurred: {error}",
        "select_model_button": "🤖 Select model",
        "toggle_image_mode_on": "🎨 Enable image mode",
        "toggle_image_mode_off": "🎨 Disable image mode",
        "add_balance_button": "💰 Top up balance",
        "help_button": "ℹ️ Help",
        "pay_50": "50 tokens - 5$",
        "pay_100": "100 tokens - 10$",
        "pay_150": "150 tokens - 15$",
        "pay_200": "200 tokens - 20$",
        "gpt_button": "GPT",
        "claude_button": "Claude",
        "free_llama_button": "🎁 FREE LLaMA",
    },
    "uk": {
        "start": "👋 Привіт, <b>{username}!</b>\nЯ бот з доступом до різних AI моделей.\n\n"
        "💰 Ваш поточний баланс: <b>{balance} токенів</b>\n"
        "🤖 Поточна модель: <b>{current_model}</b>\n\n"
        "Вартість генерації: <b>1 токен = 1 повідомлення</b>\n\n"
        "* Щоб почати використовувати нейромережу – просто напишіть текст і відправте його боту, він використовуватиме обрану вами модель.",
        "profile": "Это ваш профиль. Username: <b>{user_id}!</b> Баланс: <b>{balance}</b> Чтобы добавить баланс нажмите /pay Лимиты GPT-4o mini — осталось 29/30 o3-mini — осталось 10/10 Обновление лимитов: пятница, 28 февраля 2025 г. в 05:27 (мск)",
        "help": "ℹ️ <b>ДОВІДКА З ВИКОРИСТАННЯ БОТА</b>\n"
        "─────────────────────────\n\n"
        "🤖 <b>Доступні моделі:</b>\n"
        "• <b>GPT-4</b> - найпотужніша модель, ідеально підходить для складних завдань\n"
        "• <b>Claude 3</b> - спеціалізується на довгих діалогах та аналізі\n"
        "• <b>Together</b> - швидка модель для простих запитів\n\n"
        "💰 <b>Вартість використання:</b>\n"
        "• Текстовий запит - <b>1 токен</b>\n"
        "• Генерація зображення - <b>5 токенів</b>\n\n"
        "📝 <b>Як користуватися:</b>\n"
        "1️⃣ Виберіть AI модель\n"
        "2️⃣ Поповніть баланс\n"
        "3️⃣ Надсилайте текстові повідомлення або увімкніть режим генерації зображень\n\n"
        "⚠️ <b>ВАЖЛИВО:</b>\n"
        "Після генерації зображення не забудьте вимкнути режим зображень, "
        "щоб випадково не витратити 5 токенів на наступне повідомлення!\n\n"
        "─────────────────────────\n"
        "<i>Виберіть дію:</i>",
        "select_model": "🤖 Поточна модель: {current_model}\n\nВиберіть модель:",
        "model_changed": "✅ Модель змінено на {model}\n\nМожете надсилати повідомлення\n\nПовернутися до меню:",
        "add_balance": "💰 Виберіть суму поповнення:",
        "image_mode_on": "🎨 Режим генерації зображень <b>УВІМКНЕНО</b>\n\nНадішліть опис бажаного зображення",
        "image_mode_off": "📝 Режим генерації зображень <b>ВИМКНЕНО</b>\n\nМожете надсилати текстові повідомлення",
        "back_to_start": "👋 Головне меню\n💰 Ваш поточний баланс: {balance} токенів\n🤖 Поточна модель: {current_model}\n\nВиберіть дію:",
        "no_tokens": "❌ Недостатньо токенів. Поповніть баланс!",
        "no_image_tokens": "❌ Для генерації зображення потрібно щонайменше 5 токенів!",
        "error": "❌ Сталася помилка: {error}",
        "select_model_button": "🤖 Обрати модель",
        "toggle_image_mode_on": "🎨 Увімкнути режим зображень",
        "toggle_image_mode_off": "🎨 Вимкнути режим зображень",
        "add_balance_button": "💰 Поповнити баланс",
        "help_button": "ℹ️ Довідка",
        "pay_50": "50 токенів - 5$",
        "pay_100": "100 токенів - 10$",
        "pay_150": "150 токенів - 15$",
        "pay_200": "200 токенів - 20$",
        "gpt_button": "GPT",
        "claude_button": "Claude",
        "free_llama_button": "🎁 FREE LLaMA",
    },
}
