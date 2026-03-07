import telebot
import requests

# Apna API Token yahan dalein
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "🔥 Dragon Ball Info Bot\n\nKisi bhi Dragon Ball movie ya series ka naam likho (e.g. Dragon Ball Z, Dragon Ball Super: Super Hero).")

@bot.message_handler(func=lambda message: True)
def get_db_info(message):
    query = message.text
    # API search for Anime/Movies
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get('data', [])
            if data:
                anime = data[0]
                title = anime.get('title')
                rating = anime.get('score', 'N/A')
                img_url = anime['images']['jpg']['large_image_url']
                
                caption = (f"🎬 **Name:** {title}\n"
                           f"⭐ **Rating:** {rating}")
                
                bot.send_photo(message.chat.id, img_url, caption=caption, parse_mode="Markdown")
            else:
                bot.reply_to(message, "Maaf kijiye, ye Dragon Ball item nahi mila.")
        else:
            bot.reply_to(message, "Server busy hai, baad mein try karein.")
    except Exception:
        bot.reply_to(message, "Error! Check your connection.")

bot.infinity_polling()
            
