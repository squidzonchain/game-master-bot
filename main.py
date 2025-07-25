import os
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to $SQUIDZ 🦑\n\nThe game hasn't started yet... but you're on the list.\nType /help to prepare."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 $SQUIDZ COMMANDS:\n\n"
        "/buy - How to buy $SQUIDZ\n"
        "/chart - View the chart\n"
        "/socials - Official links\n"
        "/howtoplay - Game rules\n"
        "/tokenomics - Token info\n"
        "/rules - Group rules"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

commands = [
    BotCommand("start", "Start the game"),
    BotCommand("help", "List available commands"),
    BotCommand("buy", "How to buy $SQUIDZ"),
    BotCommand("chart", "View chart"),
    BotCommand("socials", "Social links"),
    BotCommand("howtoplay", "How to play"),
    BotCommand("tokenomics", "Tokenomics"),
    BotCommand("rules", "Group rules")
]

async def set_commands(app):
    await app.bot.set_my_commands(commands)

app.post_init(set_commands)
app.run_polling()
