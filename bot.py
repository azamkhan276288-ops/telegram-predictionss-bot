import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot ready hai ✅\n\n"
        "Tum image bhejo ya 'prediction' likho.\n"
        "Main tumhare rule ke hisaab se kaam karunga."
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "prediction":
        await update.message.reply_text(
            "⏳ Data analyse ho raha hai...\n"
            "Rule apply karke next prediction dunga (next step me full logic add hoga)."
        )
    else:
        await update.message.reply_text("Sirf image ya 'prediction' bhejo.")

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖼️ Image mil gayi\n"
        "Data read kar raha hoon...\n"
        "Rule apply karke prediction aayega."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
