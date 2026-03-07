import telebot
import requests
import os
import time

# Render Environment Variable se token lega
API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "🔥 Dragon Ball World! Kisi bhi movie ya character ka naam likho.")

@bot.message_handler(func=lambda message: True)
def get_db_info(message):
    query = message.text
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    
    try:
        # Rate limit se bachne ke liye chhota delay
        time.sleep(1)
        response = requests.get(url)
        
        if response.status_code == 200:
            res_data = response.json()
            data = res_data.get('data') # NoneType error se bachne ke liye .get use kiya
            
            if data and len(data) > 0:
                item = data[0]
                title = item.get('title', 'N/A')
                rating = item.get('score', 'N/A')
                img = item.get('images', {}).get('jpg', {}).get('large_image_url')
                
                caption = f"🎬 **Name:** {title}\n⭐ **Rating:** {rating}"
                
                if img:
                    bot.send_photo(message.chat.id, img, caption=caption, parse_mode="Markdown")
                else:
                    bot.reply_to(message, caption, parse_mode="Markdown")
            else:
                bot.reply_to(message, "❌ Kuch nahi mila! Sahi naam likho.")
        else:
            bot.reply_to(message, "⚠️ API Error! Thodi der baad try karein.")
            
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "⚠️ Connection issue!")

bot.infinity_polling()
    
