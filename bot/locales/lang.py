texts = {
    "ru": {
        "start": "👋 Привет, <b>{username}!</b>\n\nЭто бот для работы с актуальными моделями нейросетей в Telegram.\n\nКоманды:\n/start - перезапуск\n/models - выбрать нейросеть\n/profile - профиль пользователя\n/add_balance - купить подписку\n/img - генерация изображений\n/help - помощь\n\nЧтобы начьзовать нейросеть, просто напишите текст и отправьте его боту. Он будет использовать выбранную вами модель.",
        "profile": "Это ваш профиль.\n\nID: <b>{user_id}</b>\n\nБаланс: <b>{balance}</b>\n\nТекущая модель: <b>{current_model}</b>\n\nЧтобы добавить баланс нажмите /pay\n\nЛимиты: GPT-4o mini — осталось 29/30 o3-mini — осталось 10/10\n\nОбновление лимитов: пятница, 28 февраля 2025 г. в 05:27 (мск)",
        "help": "<b>О боте </b>\nБот работает через официальные API.\nМы предоставляем 10 запросов бесплатно, обновляющихся каждую неделю. Чтобы использовать бота без ограничений, вы можете приобрести подписку по команде /pay.\n\n<b>Что такое контекст?</b>\nПо умолчанию бот работает в режиме контекста, запоминая предыдущие сообщения для удобства ведения диалога в рамках одной темы. Команда /reset сбрасывает контекст.\n\n<b>Генерация изображений</b>\n- Чтобы обратиться к Midjourney или Flux, отправьте команду и текст запроса: «/img текст запроса».\n- Для генерации изображения на основе другого изображения прикрепите его к вашему запросу или вставьте ссылку на изображение.\nГенерация доступна на русском и английском языках.\n\n<i>Лимиты и подписка</i>\nЧтобы поддерживать стабильную работу без перегрузок, мы используем лимиты на генерацию. Сейчас лимиты такие:\n\nБесплатно:\n- GPT-4o mini — 30 запросов в неделю;\n- o3-mini — 10 запросов в неделю;\n\n⚡️В подписке Plus:\n- GPT-4o mini — безлимитно;\n- GPT-4o — 50 запросов в день;\n- o3-mini — 50 запросов в день;\n- GPT-4o Vision (Распознавание изображений);\n- Midjourney v6.0 — 25 запросов в день;\n- Flux.1 dev — 25 запросов в день.\n\nУправлять подпиской можно в разделе /profile.",
        "select_model": "🤖 Текущая модель: {current_model}\n\nВыберите модель:",
        "model_changed": "✅ Модель изменена на {model}\n\nМожете отправлять сообщения.",
        "add_balance": "💰 Выберите сумму пополнения:",
        "no_tokens": "❌ Недостаточно токенов. Пополните баланс!",
        "no_image_tokens": "❌ Для генерации изображения нужно минимум 5 токенов!",
        "error": "❌ Произошла ошибка: {error}",
        "pay_50": "50 токенов - 5$",
        "pay_100": "100 токенов - 10$",
        "pay_150": "150 токенов - 15$",
        "pay_200": "200 токенов - 20$",
        "gpt_button": "GPT",
        "claude_button": "Claude",
        "free_llama_button": "🎁 FREE LLaMA",
        "image_prompt_required": "Пожалуйста, добавьте текстовый промт для генерации изображения. Например: /image красивый закат над горами.",
    },
    "en": {
        "start": "👋 Hello, <b>{username}!</b>\n\nThis is a bot for working with the latest neural network models in Telegram.\n\nCommands:\n/start - restart\n/models - select a neural network\n/profile - user profile\n/add_balance - buy a subscription\n/img - image generation\n/help - help\n\nTo use the neural network, simply write a text and send it to the bot. It will use the model you selected.",
        "profile": "This is your profile.\n\nID: <b>{user_id}</b>\n\nBalance: <b>{balance}</b>\n\nCurrent model: <b>{current_model}</b>\n\nTo add balance, click /pay\n\nLimits: GPT-4o mini — 29/30 left o3-mini — 10/10 left\n\nLimit refresh: Friday, February 28, 2025 at 05:27 (MSK)",
        "help": "<b>About the bot</b>\nThe bot works through official APIs.\nWe provide 10 free requests per week. To use the bot without limits, you can purchase a subscription with the /pay command.\n\n<b>What is context?</b>\nBy default, the bot works in context mode, remembering previous messages for convenient dialogue within one topic. The /reset command resets the context.\n\n<b>Image generation</b>\n- To use Midjourney or Flux, send the command and the request text: «/img request text».\n- To generate an image based on another image, attach it to your request or paste a link to the image.\nGeneration is available in Russian and English.\n\n<i>Limits and subscription</i>\nTo maintain stable operation without overloads, we use generation limits. Current limits are:\n\nFree:\n- GPT-4o mini — 30 requests per week;\n- o3-mini — 10 requests per week;\n\n⚡️In Plus subscription:\n- GPT-4o mini — unlimited;\n- GPT-4o — 50 requests per day;\n- o3-mini — 50 requests per day;\n- GPT-4o Vision (Image recognition);\n- Midjourney v6.0 — 25 requests per day;\n- Flux.1 dev — 25 requests per day.\n\nManage your subscription in the /profile section.",
        "select_model": "🤖 Current model: {current_model}\n\nChoose a model:",
        "model_changed": "✅ Model changed to {model}\n\nYou can send messages.",
        "add_balance": "💰 Choose the top-up amount:",
        "no_tokens": "❌ Not enough tokens. Top up your balance!",
        "no_image_tokens": "❌ You need at least 5 tokens to generate an image!",
        "error": "❌ An error occurred: {error}",
        "pay_50": "50 tokens - 5$",
        "pay_100": "100 tokens - 10$",
        "pay_150": "150 tokens - 15$",
        "pay_200": "200 tokens - 20$",
        "gpt_button": "GPT",
        "claude_button": "Claude",
        "free_llama_button": "🎁 FREE LLaMA",
    },
    "uk": {
        "start": "👋 Привіт, <b>{username}!</b>\n\nЦе бот для роботи з актуальними моделями нейромереж у Telegram.\n\nКоманди:\n/start - перезапуск\n/models - обрати нейромережу\n/profile - профіль користувача\n/add_balance - придбати підписку\n/img - генерація зображень\n/help - допомога\n\nЩоб використовувати нейромережу, просто напишіть текст і надішліть його боту. Він використовуватиме обрану вами модель.",
        "profile": "Це ваш профіль.\n\nID: <b>{user_id}</b>\n\nБаланс: <b>{balance}</b>\n\nПоточна модель: <b>{current_model}</b>\n\nЩоб додати баланс, натисніть /pay\n\nЛіміти: GPT-4o mini — залишилося 29/30 o3-mini — залишилося 10/10\n\nОновлення лімітів: пʼятниця, 28 лютого 2025 р. о 05:27 (за МСК)",
        "help": "<b>Про бота</b>\nБот працює через офіційні API.\nМи надаємо 10 безкоштовних запитів на тиждень. Щоб використовувати бота без обмежень, ви можете придбати підписку за допомогою команди /pay.\n\n<b>Що таке контекст?</b>\nЗа замовчуванням бот працює в режимі контексту, запамʼятовуючи попередні повідомлення для зручного ведення діалогу в межах однієї теми. Команда /reset скидає контекст.\n\n<b>Генерація зображень</b>\n- Щоб звернутися до Midjourney або Flux, надішліть команду та текст запиту: «/img текст запиту».\n- Для генерації зображення на основі іншого зображення додайте його до вашого запиту або вставте посилання на зображення.\nГенерація доступна російською та англійською мовами.\n\n<i>Ліміти та підписка</i>\nДля підтримки стабільної роботи без перевантажень ми використовуємо ліміти на генерацію. Поточні ліміти:\n\nБезкоштовно:\n- GPT-4o mini — 30 запитів на тиждень;\n- o3-mini — 10 запитів на тиждень;\n\n⚡️У підписці Plus:\n- GPT-4o mini — безлімітно;\n- GPT-4o — 50 запитів на день;\n- o3-mini — 50 запитів на день;\n- GPT-4o Vision (Розпізнавання зображень);\n- Midjourney v6.0 — 25 запитів на день;\n- Flux.1 dev — 25 запитів на день.\n\nКерувати підпискою можна у розділі /profile.",
        "select_model": "🤖 Поточна модель: {current_model}\n\nОберіть модель:",
        "model_changed": "✅ Модель змінено на {model}\n\nМожете надсилати повідомлення.",
        "add_balance": "💰 Оберіть суму поповнення:",
        "no_tokens": "❌ Недостатньо токенів. Поповніть баланс!",
        "no_image_tokens": "❌ Для генерації зображення потрібно щонайменше 5 токенів!",
        "error": "❌ Сталася помилка: {error}",
        "pay_50": "50 токенів - 5$",
        "pay_100": "100 токенів - 10$",
        "pay_150": "150 токенів - 15$",
        "pay_200": "200 токенів - 20$",
        "gpt_button": "GPT",
        "claude_button": "Claude",
        "free_llama_button": "🎁 FREE LLaMA",
    },
}
