import os
import requests
from flask import Flask
from threading import Thread
from dotenv import load_dotenv
from telegram import Update, constants
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- KEEP ALIVE SECTION (Render Web Service Fix) ---
web_app = Flask('')

@web_app.route('/')
def home():
    return "Bot is running 24/7!"

def run():
    # Render default port 8080 use karta hai
    web_app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
# --------------------------------------------------

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Welcome message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐉 *KAMEHAMEHA!* 🐉\n\n"
        "Main Goku hoon! Mujhse Dragon Ball series ya characters ke baare mein puchiye.\n"
        "Jaise: `Dragon Ball Z` ya `Goku`", 
        parse_mode='Markdown'
    )

# Dragon Ball Search Logic
async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    
    # Dragon Ball Filter
    keywords = ["dragon ball", "goku", "vegeta", "gohan", "frieza", "broly", "dbz", "dbs"]
    if any(word in query for word in keywords):
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=constants.ChatAction.TYPING)
        
        url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
        try:
            res = requests.get(url).json()
            if res.get('data'):
                anime = res['data'][0]
                img = anime['images']['jpg']['large_image_url']
                caption = (
                    f"🐉 *DRAGON BALL SPECIAL* 🐉\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"🎬 *Title:* {anime.get('title')}\n"
                    f"⭐️ *Score:* {anime.get('score')}/10\n"
                    f"📺 *Episodes:* {anime.get('episodes')}\n"
                    f"📖 *Status:* {anime.get('status')}\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"🔥 *Powered by Snowfire AI*"
                )
                await update.message.reply_photo(photo=img, caption=caption, parse_mode='Markdown')
            else:
                await update.message.reply_text("Dragon Ball ki ye detail nahi mili! 🐉")
        except Exception as e:
            await update.message.reply_text("Z-Warriors busy hain, thoda baad mein try karein!")
    else:
        await update.message.reply_text("❌ Main sirf *Dragon Ball* ka expert hoon. Please Goku se jude sawaal puchiye! 🐉", parse_mode='Markdown')

def main():
    if not TOKEN:
        print("ERROR: Token nahi mila. Render Environment Variables check karein!")
        return
    
    # Bot start hone se pehle web server chalu karein
    keep_alive() 
    
    # Telegram Bot build
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_anime))
    
    print("🚀 Snowfire Bot is LIVE with Keep-Alive...")
    app.run_polling()

if __name__ == '__main__':
    main()
  
