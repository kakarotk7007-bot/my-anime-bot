import logging
import requests
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from keep_alive import keep_alive

# टोकन को Render की सेटिंग्स (Environment Variables) से उठाना
TOKEN = os.environ.get('BOT_TOKEN')

# ड्रैगन बॉल की 2026 जानकारी
DB_2026_INFO = (
    "🐉 **DRAGON BALL COMPLETE GUIDE (2026)** 🐉\n\n"
    "✨ **Timeline & Ratings:**\n"
    "• Dragon Ball (1986): 8.0⭐\n"
    "• Dragon Ball Z (1989): 8.8⭐\n"
    "• DB Super (2015-2026): 8.4⭐\n"
    "• DB Daima (2025): 8.1⭐\n\n"
    "🔥 **Latest Update:** Mastered Ultra Instinct Goku & Black Frieza are the top icons of 2026!"
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 नमस्ते! /info लिखें या किसी भी Anime का नाम भेजें।")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(DB_2026_INFO, parse_mode='Markdown')

async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    try:
        response = requests.get(url).json()
        if response['data']:
            anime = response['data'][0]
            res = (f"🎬 **Name:** {anime['title']}\n"
                   f"⭐ **Rating:** {anime.get('score','N/A')}/10\n"
                   f"📝 **About:** {anime.get('synopsis','')[:200]}...")
            await update.message.reply_text(res, parse_mode='Markdown')
        else:
            await update.message.reply_text("❌ जानकारी नहीं मिली।")
    except:
        await update.message.reply_text("⚠️ सर्वर एरर।")

if __name__ == '__main__':
    # Flask सर्वर शुरू करना
    keep_alive()
    
    if not TOKEN:
        print("Error: BOT_TOKEN variable not found in Render settings!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("info", info))
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), search_anime))
        
        print("🚀 बोट सफलतापूर्वक चालू हो गया है!")
        app.run_polling()
