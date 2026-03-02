import logging
import requests
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from keep_alive import keep_alive

# टोकन को Environment Variable से सुरक्षित तरीके से पढ़ना
TOKEN = os.environ.get('BOT_TOKEN')

# ड्रैगन बॉल की संपूर्ण जानकारी (2026 अपडेट)
DB_2026_INFO = (
    "🐉 **DRAGON BALL COMPLETE GUIDE (2026)** 🐉\n\n"
    "✨ **Timeline & Ratings:**\n"
    "• **Dragon Ball (1986):** 8.0⭐\n"
    "• **Dragon Ball Z (1989):** 8.8⭐\n"
    "• **DB Super (2015-2026):** 8.4⭐\n"
    "• **DB Daima (2024-2025):** 8.1⭐\n\n"
    "🔥 **Latest 2026 Stats:**\n"
    "• **Hero:** Son Goku (Ultra Instinct Mastered)\n"
    "• **Strongest Villain:** Black Frieza (Manga 2026 Arc)\n\n"
    "📢 **News:** 2026 में 40वीं सालगिरह मनाई जा रही है! सुपर सीजन 2 की आधिकारिक घोषणा जल्द होने वाली है।"
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 नमस्ते! मैं आपका 2026 एनीमे एक्सपर्ट हूँ।\n\n"
        "• /info - ड्रैगन बॉल की पूरी जानकारी\n"
        "• किसी भी Anime का नाम लिखें - मैं उसकी Rating और डिटेल बताऊंगा!"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(DB_2026_INFO, parse_mode='Markdown')

async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    
    try:
        response = requests.get(url).json()
        if response['data']:
            anime = response['data'][0]
            title = anime.get('title', 'N/A')
            rating = anime.get('score', 'N/A')
            episodes = anime.get('episodes', 'Unknown')
            synopsis = anime.get('synopsis', 'No description available.')[:250]
            
            result = (
                f"🎬 **Name:** {title}\n"
                f"⭐ **Rating:** {rating}/10\n"
                f"📺 **Episodes:** {episodes}\n"
                f"📝 **About:** {synopsis}..."
            )
            await update.message.reply_text(result, parse_mode='Markdown')
        else:
            await update.message.reply_text("❌ माफ़ कीजिये, इस एनीमे की जानकारी नहीं मिली।")
    except Exception as e:
        await update.message.reply_text("⚠️ सर्वर एरर, कृपया कुछ देर बाद कोशिश करें।")

if __name__ == '__main__':
    keep_alive() # बोट को हमेशा चालू रखने के लिए
    
    if not TOKEN:
        print("Error: 'BOT_TOKEN' नहीं मिला! Render की Environment सेटिंग्स चेक करें।")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        
        # कमांड्स और सर्च हैंडलर
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("info", info))
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), search_anime))
        
        print("🚀 बोट 2026 मोड में सुरक्षित तरीके से लाइव है!")
        app.run_polling()
  
