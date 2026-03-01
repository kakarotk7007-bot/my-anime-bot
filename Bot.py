import os
import requests
from flask import Flask
from threading import Thread
from telegram import Update, constants
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- KEEP ALIVE SECTION (Isse Render Bot ko band nahi karega) ---
web_app = Flask('')

@web_app.route('/')
def home():
    return "Goku Bot is Online! 🐉"

def run():
    # Render dynamic port use karta hai, isliye os.environ zaroori hai
    port = int(os.environ.get('PORT', 8080))
    web_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
# --------------------------------------------------------------

# Token ko Environment Variables se uthayen
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐉 *KAMEHAMEHA!* 🐉\n\n"
        "Main Goku hoon! Dragon Ball ke baare mein kuch bhi puchiye.", 
        parse_mode='Markdown'
    )

async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    keywords = ["dragon ball", "goku", "vegeta", "gohan", "frieza", "broly", "dbz", "dbs", "saiyan"]
    
    if any(word in query for word in keywords):
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=constants.ChatAction.TYPING)
        url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
        try:
            res = requests.get(url).json()
            if res.get('data'):
                anime
