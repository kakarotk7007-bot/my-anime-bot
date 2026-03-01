import os
import requests
from dotenv import load_dotenv
from telegram import Update, constants
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Token setup
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("ERROR: TELEGRAM_TOKEN nahi mila! Render settings check karein.")

# Welcome Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🐉 *Kamehameha!* Main Goku hoon. \n\nMujhse Dragon Ball ke baare mein kuch bhi puchiye!", parse_mode='Markdown')

# Dragon Ball Search Logic
async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower()
    
    # Sirf Dragon Ball filter
    if "dragon ball" in query or "goku" in query or "vegeta" in query:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=constants.ChatAction.TYPING)
        
        url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
        try:
            res = requests.get(url).json()
            if res.get('data'):
                anime = res['data'][0]
                img = anime['images']['jpg']['large_image_url']
                caption = (
                    f"🐉 *DRAGON BALL UNIVERSE* 🐉\n\n"
                    f"🎬 *Name:* {anime.get('title')}\n"
                    f"⭐️ *Rating:* {anime.get('score')}/10\n"
                    f"📺 *Episodes:* {anime.get('episodes')}\n"
                    f"🔥 *Status:* {anime.get('status')}\n\n"
                    f"Powered by Snowfire AI"
                )
                await update.message.reply_photo(photo=img, caption=caption, parse_mode='Markdown')
            else:
                await update.message.reply_text("Dragon Ball ki ye series nahi mili! 🐉")
        except:
            await update.message.reply_text("Z-Warriors busy hain, thoda ruk kar try karein!")
    else:
        await update.message.reply_text("❌ Main sirf **Dragon Ball** ka expert hoon! Goku ya Vegeta ke baare mein puchiye. 🐉")

# Main Function
def main():
    if not TOKEN: return
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_anime))
    
    print("🚀 Snowfire Bot is LIVE...")
    app.run_polling()

if __name__ == '__main__':
    main()
  
