import os
import logging
import requests
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, constants
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# 1. Token ko system environment se load karna
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- COMMAND HANDLERS ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Jab user /start likhega"""
    user = update.effective_user.first_name
    
    # Buttons setup
    keyboard = [
        [InlineKeyboardButton("🌟 Trending Anime", callback_data='trending')],
        [InlineKeyboardButton("❓ Help", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"🔥 *Namaste {user}! Snowfire Bot Active Hai!*\n\n"
        "Main aapke liye kisi bhi Anime ki detail nikaal sakta hoon.\n"
        "Bas niche Anime ka naam likh kar bhejein!",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Buttons click karne par action"""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'trending':
        await query.edit_message_text("Abhi *Naruto, One Piece aur Jujutsu Kaisen* trending mein hain! 🔥")
    elif query.data == 'help':
        await query.edit_message_text("Help: Bas anime ka naam type karein (e.g. 'Dragon Ball') aur send karein.")

# --- ANIME SEARCH LOGIC ---

async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Jikan API se Anime search karna"""
    query = update.message.text
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=constants.ChatAction.TYPING)
    
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    
    try:
        res = requests.get(url, timeout=15).json()
        if res.get('data'):
            anime = res['data'][0]
            title = anime.get('title_english') or anime.get('title')
            img = anime['images']['jpg']['large_image_url']
            
            caption = (
                f"🎬 *NAME:* {title}\n"
                f"⭐️ *SCORE:* {anime.get('score', 'N/A')}\n"
                f"📺 *EPISODES:* {anime.get('episodes', 'Ongoing')}\n"
                f"🎭 *GENRES:* {', '.join([g['name'] for g in anime.get('genres', [])])}\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"✨ *Powered by Snowfire*"
            )
            await update.message.reply_photo(photo=img, caption=caption, parse_mode='Markdown')
        else:
            await update.message.reply_text("❌ Maaf kijiye, ye Anime nahi mila.")
    except Exception as e:
        await update.message.reply_text("⚠️ API Error! Thodi der baad try karein.")

# --- MAIN RUNNER ---

def main():
    if not TOKEN:
        print("❌ ERROR: TELEGRAM_TOKEN nahi mila! .env file check karein.")
        return

    app = Application.builder().token(TOKEN).build()
    
    # Handlers register karna
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_anime))
    
    print("🚀 Snowfire Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
          
