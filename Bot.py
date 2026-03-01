import os
import requests
from flask import Flask
from threading import Thread
from telegram import Update, constants
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- KEEP ALIVE SECTION (Render aur UptimeRobot ke liye) ---
web_app = Flask('')

@web_app.route('/')
def home():
    # Jab UptimeRobot is link par aayega, toh ye message dikhega
    return "Goku Bot is Online and Guarding the Dragon Balls! 🐉"

def run():
    # Render dynamic port use karta hai, isliye os.environ zaroori hai
    port = int(os.environ.get('PORT', 8080))
    web_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
# ---------------------------------------------------------

# Token ko Render ke Environment Variables se uthayen
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Welcome message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐉 *KAMEHAMEHA!* 🐉\n\n"
        "Main Goku hoon! Mujhse Dragon Ball series ya characters ke baare mein puchiye.", 
        parse_mode='Markdown'
    )

# Dragon Ball Search Logic (Fixed with Try-Except)
async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    
    # Dragon Ball Filter
    keywords = ["dragon ball", "goku", "vegeta", "gohan", "frieza", "broly", "dbz", "dbs", "saiyan"]
    
    if any(word in query for word in keywords):
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=constants.ChatAction.TYPING)
        
        url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
        try:
            res = requests.get(url).json()
            if res.get('data') and len(res['data']) > 0:
                anime = res['data'][0]
                img = anime['images']['jpg']['large_image_url']
                caption = (
                    f"🐉 *DRAGON BALL SPECIAL* 🐉\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"🎬 *Title:* {anime.get('title')}\n"
                    f"⭐️ *Score:* {anime.get('score')}/10\n"
                    f"🔥 *Powered by Snowfire AI*"
                )
                await update.message.reply_photo(photo=img, caption=caption, parse_mode='Markdown')
            else:
                await update.message.reply_text("Dragon Ball ki ye detail nahi mili! 🐉")
        except Exception as e:
            print(f"Error: {e}")
            await update.message.reply_text("Z-Warriors busy hain, thoda baad mein try karein!")
    else:
        await update.message.reply_text("❌ Main sirf *Dragon Ball* ka expert hoon. Please Goku se jude sawaal puchiye! 🐉", parse_mode='Markdown')

def main():
    if not TOKEN:
        print("ERROR: TELEGRAM_TOKEN nahi mila! Render ki settings check karein.")
        return
    
    # Bot start hone se pehle web server chalu karein
    keep_alive() 
    
    # Telegram Bot build
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_anime))
    
    print("🚀 Bot is LIVE...")
    app.run_polling()

if __name__ == '__main__':
    main()
