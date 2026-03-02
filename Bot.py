import os
import telebot
import requests
from keep_alive import keep_alive

# यह लाइन रेंडर की सेटिंग्स से 'TOKEN' नाम का वेरिएबल उठाएगी
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# सर्वर को 24/7 चालू रखने के लिए
keep_alive()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "नमस्ते! किसी भी एनीमे का नाम लिखें और मैं उसकी फोटो और रेटिंग ढूँढ कर दूँगा।")

@bot.message_handler(func=lambda message: True)
def search_anime(message):
    query = message.text
    # Jikan API का इस्तेमाल करके एनीमे सर्च करना
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['data']:
            anime = data['data'][0]
            img = anime['images']['jpg']['large_image_url']
            title = anime['title']
            score = anime.get('score', 'N/A')
            
            caption = f"🌟 **नाम:** {title}\n⭐ **रेटिंग:** {score}/10"
            bot.send_photo(message.chat.id, img, caption=caption, parse_mode="Markdown")
        else:
            bot.reply_to(message, "क्षमा करें, इस नाम का कोई एनीमे नहीं मिला।")
    except Exception as e:
        bot.reply_to(message, "⚠️ सर्वर एरर! कृपया दोबारा कोशिश करें।")

# बोट को रन करना
if __name__ == "__main__":
    bot.polling(none_stop=True)
