"""
Бот, который открывает мини-приложение внутри Telegram.

Запуск:
    pip install python-telegram-bot
    export BOT_TOKEN="8818036112:AAFgR0NtXEFQYMDYy_DN3a582NSIq89YgOg"
    export WEBAPP_URL="https://tbilisipay.netlify.app/"
    python miniapp_bot.py
"""
import os

from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp,
                      Update, WebAppInfo)
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

WEBAPP_URL = os.environ["WEBAPP_URL"]

WELCOME = (
    "<b>Перевод в Грузию через Wallet</b>\n\n"
    "Помогу провести перевод по шагам: от покупки USDT в Wallet "
    "до передачи мне данных получателя.\n\n"
    "Открой приложение, чтобы начать."
)


async def post_init(app: Application) -> None:
    # Кнопка-меню рядом со строкой ввода
    await app.bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Открыть", web_app=WebAppInfo(url=WEBAPP_URL))
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("Открыть", web_app=WebAppInfo(url=WEBAPP_URL))
    ]])
    await update.message.reply_text(WELCOME, reply_markup=kb, parse_mode=ParseMode.HTML)


def main() -> None:
    app = Application.builder().token(os.environ["BOT_TOKEN"]).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
