"""
💖 БОТ ЛЮБВИ
Создан с любовью для тебя
Автор: [Ваше имя]
"""

import os
import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ================= НАСТРОЙКА =================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота (получите у @BotFather)
TOKEN = os.environ.get("TOKEN", "ВАШ_ТОКЕН_ЗДЕСЬ")  # Для облака используйте переменную окружения TOKEN

# ================= БАЗА ДАННЫХ ВАШИХ ЧУВСТВ =================
# ВНИМАНИЕ: Замените всё, что в квадратных скобках, на СВОИ личные слова!

# Причины, почему я тебя люблю
LOVE_REASONS = [
    "[ЗАМЕНИ_ЭТО] Я люблю тебя за твою улыбку, которая освещает даже самый пасмурный день.",
    "[ЗАМЕНИ_ЭТО] Я люблю тебя за то, как ты заботишься обо мне, даже когда сама устала.",
    "[ЗАМЕНИ_ЭТО] Я люблю тебя за твой смех — он самый искренний звук в моей жизни.",
    "[ЗАМЕНИ_ЭТО] Я люблю тебя за твою доброту к людям и животным.",
    "[ЗАМЕНИ_ЭТО] Я люблю тебя за то, как ты хмуришь бровки, когда сосредоточена.",
    "[ЗАМЕНИ_ЭТО] Я люблю тебя за наши разговоры до утра.",
    "[ЗАМЕНИ_ЭТО] Я люблю тебя за то, что с тобой я могу быть собой.",
    "[ЗАМЕНИ_ЭТО] Я люблю тебя за твои маленькие привычки, которые стали такими родными.",
    "[ЗАМЕНИ_ЭТО] Я люблю тебя за то, как ты поддерживаешь меня в трудные моменты.",
    "[ЗАМЕНИ_ЭТО] Я люблю тебя просто потому, что ты есть.",
    # ↓↓↓ ДОПИШИТЕ ЕЩЕ СВОИ ПРИЧИНЫ ↓↓↓
]

# Комплименты
COMPLIMENTS = [
    "[ЗАМЕНИ_ЭТО] Ты сегодня невероятно красива.",
    "[ЗАМЕНИ_ЭТО] Твои глаза сегодня особенно сияют.",
    "[ЗАМЕНИ_ЭТО] С тобой даже обычный день становится праздником.",
    "[ЗАМЕНИ_ЭТО] Твое присутствие делает мир лучше.",
    "[ЗАМЕНИ_ЭТО] Ты самая теплая и уютная вселенная.",
    # ↓↓↓ ДОПИШИТЕ ЕЩЕ СВОИХ КОМПЛИМЕНТОВ ↓↓↓
]

# Воспоминания
MEMORIES = [
    "[ЗАМЕНИ_ЭТО] Помнишь, как мы впервые встретились? [Опишите этот момент]",
    "[ЗАМЕНИ_ЭТО] Наше первое свидание... [Опишите подробно]",
    "[ЗАМЕНИ_ЭТО] Тот вечер, когда мы впервые... [Ваше особое воспоминание]",
    # ↓↓↓ ДОБАВЬТЕ СВОИ ВОСПОМИНАНИЯ ↓↓↓
]

# Слова поддержки
SUPPORT_WORDS = [
    "[ЗАМЕНИ_ЭТО] Я всегда буду рядом, что бы ни случилось.",
    "[ЗАМЕНИ_ЭТО] Ты сильнее, чем думаешь, и я верю в тебя.",
    "[ЗАМЕНИ_ЭТО] Просто помни: я тебя люблю, и это главное.",
    "[ЗАМЕНИ_ЭТО] Всё будет хорошо, я обещаю.",
    # ↓↓↓ ДОБАВЬТЕ СВОИ СЛОВА ПОДДЕРЖКИ ↓↓↓
]

# ================= ФУНКЦИИ БОТА =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /start - первое впечатление"""
    user = update.effective_user
    
    welcome_text = f"""
💖 *Привет, дорогая!*

Этот бот — мое любовное письмо в цифровом мире.
Здесь живут все мои чувства к тебе.

*Просто выбери, что хочешь получить:*
❤️ /love — узнать, почему я тебя люблю
✨ /compliment — получить комплимент
📸 /memory — вспомнить наш момент
🤗 /support — слова поддержки
💬 /talk — просто поговорить
❓ /help — все команды

Или просто напиши мне что-нибудь — я отвечу с любовью!

*Всегда твой,*
[Ваше имя]
    """
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def send_love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Случайная причина любви"""
    if not LOVE_REASONS:
        reason = "Я люблю тебя просто потому, что ты — это ты."
    else:
        reason = random.choice(LOVE_REASONS)
    
    # Красивое оформление с сердечками
    hearts = ["❤️", "💖", "💕", "💗", "💓"]
    heart_line = " ".join([random.choice(hearts) for _ in range(5)])
    
    await update.message.reply_text(
        f"{heart_line}\n"
        f"💌 *Я люблю тебя потому что:*\n\n"
        f"{reason}\n"
        f"{heart_line}",
        parse_mode='Markdown'
    )

async def send_compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Случайный комплимент"""
    compliment = random.choice(COMPLIMENTS) if COMPLIMENTS else "Ты прекрасна!"
    
    emojis = ["✨", "🌟", "💫", "⭐", "🌸", "🌺", "🌹", "💐"]
    emoji = random.choice(emojis)
    
    await update.message.reply_text(
        f"{emoji} *Для тебя, моя любимая:*\n\n"
        f"«{compliment}»\n\n"
        f"Это правда, от всего сердца {emoji}",
        parse_mode='Markdown'
    )

async def send_memory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Общее воспоминание"""
    if not MEMORIES:
        memory_text = "Каждый момент с тобой — это отдельное прекрасное воспоминание."
    else:
        memory_text = random.choice(MEMORIES)
    
    await update.message.reply_text(
        f"📸 *Давай вспомним...*\n\n"
        f"{memory_text}\n\n"
        f"💭 Этот момент навсегда в моем сердце",
        parse_mode='Markdown'
    )

async def send_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Слова поддержки"""
    if not SUPPORT_WORDS:
        support_text = "Я здесь, я с тобой, и всё будет хорошо."
    else:
        support_text = random.choice(SUPPORT_WORDS)
    
    await update.message.reply_text(
        f"🤗 *Обнимаю крепко и говорю:*\n\n"
        f"{support_text}\n\n"
        f"💪 Ты не одна, я всегда рядом",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Помощь по командам"""
    help_text = """
💝 *Доступные команды:*

❤️ `/love` — Узнать причину моей любви
✨ `/compliment` — Получить персональный комплимент
📸 `/memory` — Вспомнить наш особенный момент
🤗 `/support` — Слова поддержки и ободрения
💬 `/talk` — Просто поговорить со мной
❓ `/help` — Эта справка

*Или просто напиши:*  
• "люблю" — и я скажу, как люблю тебя  
• "скучаю" — и я скажу, как скучаю  
• "привет" — для теплого приветствия  
• "как дела" — узнай, как я  
• любое другое слово — и я отвечу с любовью 💖

*С любовью,*  
[Ваше имя]
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def talk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Просто поболтать"""
    responses = [
        "Я так рад, что ты написала! 💖",
        "Как же я по тебе скучал... 💫",
        "Твоё сообщение сделало мой день лучше! 🌸",
        "Думаю о тебе каждый день, каждую минуту 💭",
        "Жду нашей встречи, моя любимая 🌙",
        "Ты — лучшее, что есть в моей жизни ✨"
    ]
    
    await update.message.reply_text(random.choice(responses))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка обычных сообщений"""
    user_message = update.message.text.lower()
    
    # Ответы на ключевые слова
    keyword_responses = {
        "люблю": [
            "И я тебя люблю! Больше всего на свете 💖",
            "Знаю, и это взаимно! Моё сердце твоё 💕", 
            "Спасибо, что говоришь это... Я люблю тебя сильнее с каждым днём 🥰",
            "Эти слова делают меня счастливым! Я тоже безумно тебя люблю 💘"
        ],
        "скучаю": [
            "Я тоже по тебе скучаю... Каждую секунду 💫",
            "Скоро увидимся, моя радость! 🌙",
            "Держи мысленно за руку и жди встречи 🤝",
            "Представь, что я обнимаю тебя прямо сейчас 🤗"
        ],
        "привет": [
            "Привет, солнышко моё! ☀️",
            "Здравствуй, самая красивая девушка на свете 💐",
            "Привет-привет! Как я рад тебя видеть! 👋",
            "О, моя любимая зашла в бота! Приветствую! 💖"
        ],
        "как дела": [
            "Всё хорошо, особенно когда думаю о тебе! 🌸",
            "Отлично! А у тебя, моя хорошая? 💖",
            "Стало лучше, как только ты написала! ✨",
            "Скучаю по тебе, но в остальном всё прекрасно 💫"
        ],
        "спокойной ночи": [
            "Спокойной ночи, ангел мой 🌙 Сладких снов 💫",
            "Спи крепко, моя любимая 💤 Обнимаю мысленно 🤗",
            "Приятных снов, пусть тебе приснится что-то прекрасное 💭",
            "Спокойной ночи, засыпай с мыслью, что я люблю тебя 💖"
        ],
        "доброе утро": [
            "Доброе утро, солнце! ☀️ Как спалось?",
            "С добрым утром, моя радость! 🌸 Хорошего дня!",
            "Утро стало добрым, потому что ты написала! 💖",
            "Доброе утро, красавица! Пусть день будет чудесным ✨"
        ]
    }
    
    # Проверяем ключевые слова
    for keyword, answer_list in keyword_responses.items():
        if keyword in user_message:
            await update.message.reply_text(random.choice(answer_list))
            return
    
    # Если не нашли ключевое слово - случайный любовный ответ
    random_responses = [
        "Ты делаешь мой мир лучше просто своим существованием 💖",
        "Как же я тебя люблю... Иногда даже словами не передать 🌹",
        "Просто знай: ты самая лучшая девушка на свете ✨",
        "С тобой я счастлив по-настоящему 💕",
        "Каждый раз, когда ты пишешь, я улыбаюсь 😊",
        "Ты — моё самое большое счастье 💫"
    ]
    
    await update.message.reply_text(random.choice(random_responses))

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка ошибок"""
    logger.error(f"Ошибка: {context.error}")
    try:
        await update.message.reply_text("💔 Что-то пошло не так... Но моя любовь к тебе вечна и непоколебима! 💖")
    except:
        pass

# ================= ЗАПУСК БОТА =================
def main():
    """Основная функция запуска"""
    print("=" * 50)
    print("💖 ЗАПУСКАЕТСЯ БОТ ЛЮБВИ...")
    print("=" * 50)
    
    if TOKEN == "ВАШ_ТОКЕН_ЗДЕСЬ":
        print("⚠️  ВНИМАНИЕ: Токен не установлен!")
        print("\nКак получить токен:")
        print("1. Найди в Telegram @BotFather")
        print("2. Напиши /newbot и следуй инструкциям")
        print("3. Скопируй полученный токен")
        print("4. Замени 'ВАШ_ТОКЕН_ЗДЕСЬ' на свой токен")
        print("\nИЛИ для облачного хостинга:")
        print("Установи переменную окружения TOKEN")
        print("=" * 50)
        return
    
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем команды
    commands = [
        ("start", start),
        ("love", send_love),
        ("compliment", send_compliment),
        ("memory", send_memory),
        ("support", send_support),
        ("help", help_command),
        ("talk", talk),
    ]
    
    for command, handler in commands:
        application.add_handler(CommandHandler(command, handler))
    
    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Обработчик ошибок
    application.add_error_handler(error_handler)
    
    # Проверяем наполнение базы данных
    print("\n📊 ПРОВЕРКА ВАШИХ СООБЩЕНИЙ:")
    print(f"   ❤️  Причин любви: {len(LOVE_REASONS)}")
    print(f"   ✨ Комплиментов: {len(COMPLIMENTS)}")
    print(f"   📸 Воспоминаний: {len(MEMORIES)}")
    print(f"   🤗 Слов поддержки: {len(SUPPORT_WORDS)}")
    
    if "[ЗАМЕНИ_ЭТО]" in str(LOVE_REASONS + COMPLIMENTS + MEMORIES + SUPPORT_WORDS):
        print("\n⚠️  ВАЖНОЕ НАПОМИНАНИЕ:")
        print("   Замени ВСЕ '[ЗАМЕНИ_ЭТО]' на свои личные слова!")
        print("   Это сделает бота уникальным и по-настоящему твоим!")
    
    print("\n" + "=" * 50)
    print("✅ Бот готов к работе!")
    print("🔗 Ссылка на бота: t.me/ваш_бот (замени на реальную)")
    print("=" * 50)
    print("\n💝 Советы по наполнению:")
    print("   • Пиши от сердца, будь искренним")
    print("   • Вспоминай конкретные моменты")
    print("   • Используй ваши личные шутки")
    print("   • Добавь хотя бы 20-30 своих фраз в каждый раздел")
    print("=" * 50)
    
    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)

if __name__ == '__main__':
    main()