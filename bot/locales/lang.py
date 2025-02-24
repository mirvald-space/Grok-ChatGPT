texts = {
    "ru": {
        "start": "👋 Привет, <b>{username}!</b>\n\nЭто бот для работы с актуальными моделями нейросетей в Telegram.\n\nКоманды:\n/start - перезапуск\n/models - выбрать нейросеть\n/profile - профиль пользователя\n/image - генерация изображений\n/help - помощь\n\nЧтобы начать использовать нейросеть, просто напишите текст и отправьте его боту. Он будет использовать выбранную вами модель.",
        "profile": "Это ваш профиль.\n\nID: <b>{user_id}</b>\n\nБаланс: <b>{balance}</b>\n\nТекущая модель: <b>{current_model}</b>",
        "help": "<b>О боте </b>\nБот работает через официальные API.\nМы предоставляем 10 бесплатных запросов, обновляющихся каждый день. \n\n<b>Генерация изображений</b>\nЧтобы cгенерировать изображение, отправьте команду и текст запроса: «/image текст запроса».\n\n<i>Лимиты</i>\nЧтобы поддерживать стабильную работу без перегрузок, мы используем лимиты на генерацию.",
        "select_model": "🤖 Текущая модель: {current_model}\n\nВыберите модель:",
        "model_changed": "✅ Модель изменена на {model}\n\nМожете отправлять сообщения.",
        "no_tokens": "❌ Недостаточно токенов.",
        "no_image_tokens": "❌ Для генерации изображения нужно минимум 5 токенов!",
        "error": "❌ Произошла ошибка: {error}",
        "access_denied": "👋 Привет, <b>{username}!</b>\n\nЧтобы получить доступ к боту и сделать вашу работу проще и эффективнее\n\n- Необходимо пригласить одного пользователя в бот.\n\nВаша реферальная ссылка:\n\n{invite_link}",
        "invite_link": "Ваша ссылка для приглашения: {invite_link}",
        "gpt_button": "GPT-4o",
        "grok_button": "Grok",
        "claude_button": "Claude",
        "free_llama_button": "DeepSeek V3",
        "image_prompt_required": "Пожалуйста, добавьте текстовый запрос для генерации изображения. Например: /image красивый закат над горами.",
        "start_description": "Начало работы",
        "models_description": "Выбрать нейросеть",
        "image_description": "Генерация изображения",
        "invite_description": "Пригласить друзей",
        "profile_description": "Профиль",
        "help_description": "Помощь",
    },
    "en": {
        "start": "👋 Hello, <b>{username}!</b>\n\nThis is a bot for working with the latest neural network models in Telegram.\n\nCommands:\n/start - restart\n/models - select a neural network\n/profile - user profile\n/image - image generation\n/help - help\n\nTo start using the neural network, simply write a text and send it to the bot. It will use the model you selected.",
        "profile": "This is your profile.\n\nID: <b>{user_id}</b>\n\nBalance: <b>{balance}</b>\n\nCurrent model: <b>{current_model}</b>",
        "help": "<b>About the bot</b>\nThe bot works through official APIs.\nWe provide 10 free requests per day.\n\n<b>What is context?</b>\n<b>Image generation</b>\nTo generate an image, send the command and request text: «/image request text».\n\n<i>Limits</i>\nTo maintain stable operation without overloads, we use generation limits.",
        "select_model": "🤖 Current model: {current_model}\n\nChoose a model:",
        "model_changed": "✅ Model changed to {model}\n\nYou can send messages.",
        "no_tokens": "❌ Not enough tokens.",
        "no_image_tokens": "❌ You need at least 5 tokens to generate an image!",
        "error": "❌ An error occurred: {error}",
        "access_denied": "👋 Hi, <b>{username}!</b>\n\nTo access the bot and make your work easier and more efficient\n\n- You need to invite one user to the bot.\n\nYour referral link:\n\n{invite_link}",
        "invite_link": "Your invite link: {invite_link}",
        "gpt_button": "GPT-4o",
        "claude_button": "Claude",
        "grok_button": "Grok",
        "free_llama_button": "DeepSeek V3",
        "image_prompt_required": "Please add a text query to generate the image. For example: /image beautiful sunset over the mountains.",
        "start_description": "Start working",
        "models_description": "Choose a neural network",
        "image_description": "Generate an image",
        "invite_description": "Invite friends",
        "profile_description": "Profile",
        "help_description": "Help",
    },
    "uk": {
        "start": "👋 Привіт, <b>{username}!</b>\n\nЦе бот для роботи з актуальними моделями нейромереж у Telegram.\n\nКоманди:\n/start - перезапуск\n/models - обрати нейромережу\n/profile - профіль користувача\n/image - генерація зображень\n/help - допомога\n\nЩоб почати використовувати нейромережу, просто напишіть текст і надішліть його боту. Він використовуватиме обрану вами модель.",
        "profile": "Це ваш профіль.\n\nID: <b>{user_id}</b>\n\nБаланс: <b>{balance}</b>\n\nПоточна модель: <b>{current_model}</b>",
        "help": "<b>Про бота</b>\nБот працює через офіційні API.\nМи надаємо 10 безкоштовних запитів на день.\n\n<b>Генерація зображень</b>\nЩоб згенерувати зображення, надішліть команду та текст запиту: «/image текст запиту».\n\n<i>Ліміти</i>\nДля підтримки стабільної роботи без перевантажень ми використовуємо ліміти на генерацію.",
        "select_model": "🤖 Поточна модель: {current_model}\n\nОберіть модель:",
        "model_changed": "✅ Модель змінено на {model}\n\nМожете надсилати повідомлення.",
        "no_tokens": "❌ Недостатньо токенів.",
        "no_image_tokens": "❌ Для генерації зображення потрібно щонайменше 5 токенів!",
        "error": "❌ Сталася помилка: {error}",
        "access_denied": "👋 Привіт, <b>{username}!</b>\n\nЩоб отримати доступ до боту і зробити вашу роботу простішою та ефективнішою -Необхідно запросити одного друга в бот.\n\nВаше реферальне посилання:\n\n{invite_link}",
        "invite_link": "Ваша реферальна посилання: {invite_link}",
        "gpt_button": "GPT-4o",
        "claude_button": "Claude",
        "grok_button": "Grok",
        "free_llama_button": "DeepSeek V3",
        "image_prompt_required": "Будь ласка, додайте текстовий запит для генерації зображення. Наприклад: /image красивий захід сонця над горами.",
        "start_description": "Початок роботи",
        "models_description": "Вибрати нейромережу",
        "image_description": "Генерація зображення",
        "invite_description": "Запросити друзів",
        "profile_description": "Профіль",
        "help_description": "Допомога",
    },
}
