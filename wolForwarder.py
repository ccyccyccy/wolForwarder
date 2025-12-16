#!/usr/bin/env python

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from wakeonlan import send_magic_packet
import os

load_dotenv()
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN") or ''

if not TELEGRAM_API_TOKEN:
    print("NO API TOKEN. EXITING...")
    exit()


async def wakePc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    send_magic_packet('B4.2E.99.A1.21.2F')
    await update.message.reply_text('Trying to wake PC...')


def main() -> None:
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    # application.add_handler(CommandHandler(["g", "G"], wakePc))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, wakePc))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
