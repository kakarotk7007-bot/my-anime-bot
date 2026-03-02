import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# लॉगिंग ताकि आप Render पर एरर देख सकें
logging.basicConfig(level=logging.INFO)

async def search_anime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text # यूज़र ने जो लिखा
    await update.message.reply_chat_action(action="typing")

    # Jikan API का इस्तेमाल करके एनीमे सर्च करना
    # यह 'q' पैरामीटर में यूज़र का लिखा हुआ नाम भेजता है
    search_url = f"https://api.jikan.moe/v4/anime?q={user_query}&limit=1"

    try:
        response = requests.get(search_url)
        data = response.json()

        if data['data']:
            anime = data['data'][0] # सबसे पहला रिजल्ट
            title = anime['title']
            rating = anime.get('score', 'N/A')
            synopsis = anime.get('synopsis', 'जानकारी उपलब्ध नहीं है।')[:300] + "..."
            image_url = anime['images']['jpg']['large_image_url']
            anime_url = anime['url']

            caption = f"🌟 **नाम:** {title}\n⭐ **रेटिंग:** {rating}/10\n\n📖 **कहानी:** {synopsis}\n\n🔗 [यहाँ और देखें]({anime_url})"
            
            # फोटो और जानकारी भेजना
            await update.message.reply_photo(photo=image_url, caption=caption, parse_mode="Markdown")
        else:
            await update.message.reply_text(f"क्षमा करें, मुझे '{user_query}' नाम का कोई एनीमे नहीं मिला।")

    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text("⚠️ सर्वर एरर! कृपया दोबारा कोशिश करें।")

if __name__ == '__main__':
    # अपना असली टोकन यहाँ डालें
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), search_anime))
    
    # Render को 24/7 जगाए रखने के लिए (Flask)
    from flask import Flask
    from threading import Thread
    import os

    server = Flask('')
    @server.route('/')
    def home(): return "Bot is Running"
    def run(): server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
    Thread(target=run).start()

    app.run_polling()
  
