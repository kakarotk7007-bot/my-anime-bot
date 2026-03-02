import os
import telebot
import requests
from keep_alive import keep_alive

# यह लाइन रेंडर की 'Environment Variables' से टोकन सुरक्षित तरीके से लेगी
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

keep_alive()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "नमस्ते! किसी भी एनीमे का नाम लिखें।")

@bot.message_handler(func=lambda message: True)
def search_anime(message):
    query = message.text
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    try:
        response = requests.get(url)
        data = response.json()
        if data['data']:
            anime = data['data'][0]
            img = anime['images']['jpg']['large_image_url']
            caption = f"🌟 **नाम:** {anime['title']}\n⭐ **रेटिंग:** {anime.get('score', 'N/A')}/10"
            bot.send_photo(message.chat.id, img, caption=caption, parse_mode="Markdown")
        else:
            bot.reply_to(message, "एनीमे नहीं मिला।")
    except Exception:
        bot.reply_to(message, "⚠️ एरर!")

if __name__ == "__main__":
    bot.polling(none_stop=True)
  
