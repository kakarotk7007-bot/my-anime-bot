import os
import requests
from flask import Flask
from threading import Thread
from telegram import Update, constants
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- WEB SERVER (Keep-Alive ke liye) ---
web_app = Flask('')

@web_app.route('/')
def home():
    return "Goku Bot is Online! 🐉"

def run():
    # Render dynamic port use karta hai
    port = int(os.environ.get('PORT', 8080))
    web_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# --- BOT LOGIC ---
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🐉 *KAMEHAMEHA!* 🐉\nMain Goku hoon!")

async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    
    try:
        res = requests.get(url).json()
        if res.get('data'):
            anime = res['data'][0]
            img = anime['images']['jpg']['large_image_url']
            await update.message.reply_photo(photo=img, caption=f"🐉 Found: {anime.get('title')}")
        else:
            await update.message.reply_text("Nahi mila!")
    except Exception as e:
        print(f"Error: {e}") # Debugging ke liye
        await update.message.reply_text("Z-Warriors busy hain!")

def main():
    if not TOKEN:
        return
    
    keep_alive() 
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_anime))
    app.run_polling()

if __name__ == '__main__':
    main()
