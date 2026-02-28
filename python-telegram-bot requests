import logging  # Fixed: lowercase 'i'
import requests 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.constants import ChatAction

# --- YAHAN NAYA TOKEN DAALEIN ---
# Reminder: Revoke this token in BotFather and paste the new one here!
TOKEN = "8458249103:AAEaxeI8QimwB_au4RFJSEerVJSOfYiLHz8"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❄️ Snowfire AI Ready! 🔥\nAnime ka naam likhein!")

async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    if not query: return
    
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    
    try:
        search_url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
        res = requests.get(search_url, timeout=15).json()
        
        if res.get('data') and len(res['data']) > 0:
            anime = res['data'][0]
            a_id = anime['mal_id']
            
            c_url = f"https://api.jikan.moe/v4/anime/{a_id}/characters"
            c_res = requests.get(c_url, timeout=10).json()
            
            hero = "N/A"
            if c_res.get('data') and len(c_res['data']) > 0:
                hero = c_res['data'][0]['character']['name']
            
            title = anime.get('title_english') or anime.get('title') or "Unknown"
            score = anime.get('score', 'N/A')
            rating = anime.get('rating', 'N/A')
            aired = anime.get('aired', {}).get('string', 'N/A')
            status = anime.get('status', 'N/A')
            studio = ", ".join([s['name'] for s in anime.get('studios', [])]) or "N/A"
            
            # Using HTML parse mode because Markdown can sometimes break with special characters
            caption = (
                f"🎬 <b>NAME:</b> {title}\n"
                f"👤 <b>HERO:</b> {hero}\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"⭐️ <b>SCORE:</b> {score}/10\n"
                f"🔞 <b>RATING:</b> {rating}\n"
                f"📅 <b>AIRED:</b> {aired}\n"
                f"📊 <b>STATUS:</b> {status}\n"
                f"🎨 <b>STUDIO:</b> {studio}\n"
                f"━━━━━━━━━━━━━━━━━━━━"
            )
            img = anime['images']['jpg']['large_image_url']
            await update.message.reply_photo(photo=img, caption=caption, parse_mode='HTML')
        else:
            await update.message.reply_text("Nahi mila! ❌")
    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text("Kuch error aaya, dobara try karein!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_anime))
    
    print("Snowfire Bot is Starting...")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':  # Fixed: added double underscores
    main()
