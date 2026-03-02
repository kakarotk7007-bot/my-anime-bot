import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from keep_alive import keep_alive # बोट को हमेशा चालू रखने के लिए

# 1. आपका टोकन (इसे सुरक्षित रखें)
TOKEN = '8710944697:AAGX0bRsQbQTeyGohpPbn6B_uGUyRfqUdTg'

# 2. ड्रैगन बॉल की 2026 की फिक्स्ड जानकारी
DB_2026_INFO = (
    "🐉 **DRAGON BALL COMPLETE GUIDE 2026** 🐉\n\n"
    "📅 **Timeline:**\n"
    "• Dragon Ball (1986): 8.0⭐\n"
    "• Dragon Ball Z (1989): 8.8⭐\n"
    "• Dragon Ball Super (2015-2026): 8.4⭐\n"
    "• Dragon Ball Daima (2025): 8.1⭐\n\n"
    "🔥 **Latest Update:**\n"
    "2026 में मंगा में 'Black Frieza Arc' चल रहा है और 'DBS Season 2' की घोषणा जल्द होने वाली है।\n"
    "मुख्य हीरो: Son Goku (Ultra Instinct Level)"
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# स्टार्ट कमांड
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "नमस्ते! मैं आपका ऑल-इन-वन एनीमे बोट हूँ।\n\n"
        "• /info - ड्रैगन बॉल की पूरी जानकारी के लिए।\n"
        "• किसी भी एनीमे का नाम लिखें - मैं उसकी पूरी डिटेल दूंगा!"
    )

# ड्रैगन बॉल की जानकारी
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(DB_2026_INFO, parse_mode='Markdown')

# किसी भी एनीमे को इंटरनेट पर सर्च करने वाला फंक्शन
async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text
    # API URL (Jikan API for MyAnimeList)
    url = f"https://api.jikan.moe/v4/anime?q={user_query}&limit=1"
    
    try:
        response = requests.get(url).json()
        if response['data']:
            anime = response['data'][0]
            
            # डेटा निकालना
            title = anime.get('title', 'N/A')
            rating = anime.get('score', 'N/A')
            episodes = anime.get('episodes', 'Unknown')
            synopsis = anime.get('synopsis', 'No description available.')
            
            result_text = (
                f"🎬 **Name:** {title}\n"
                f"⭐ **Rating:** {rating}/10\n"
                f"📺 **Episodes:** {episodes}\n"
                f"📝 **About:** {synopsis[:300]}..."
            )
            await update.message.reply_text(result_text, parse_mode='Markdown')
        else:
            await update.message.reply_text("❌ माफ़ कीजिये, मुझे इस नाम का कोई एनीमे नहीं मिला।")
    except Exception as e:
        await update.message.reply_text("⚠️ सर्वर अभी व्यस्त है, कृपया कुछ देर बाद कोशिश करें।")

if __name__ == '__main__':
    # 24/7 चालू रखने के लिए Flask सर्वर शुरू करना
    keep_alive()
    
    # बोट शुरू करना
    app = ApplicationBuilder().token(TOKEN).build()
    
    # कमांड्स और मैसेज हैंडलर को जोड़ना
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    # यह लाइन हर टेक्स्ट मैसेज को सर्च करेगी
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), search_anime))
    
    print("✅ बोट सफलतापूर्वक चालू हो गया है!")
    app.run_polling()
          
