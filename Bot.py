import telebot
import requests
import os
import time

# Render Environment Variable 'BOT_TOKEN' se connect karega
API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    # Bot ke start hote hi user ko instruction dena
    bot.reply_to(message, "🥋 **Dragon Ball Master Bot v2**\n\nKoi bhi series ya character ka naam likho:\n- Dragon Ball Z\n- Dragon Ball Super: Super Hero\n- Ultra Instinct Goku\n- Beerus", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def dragon_ball_search(message):
    query = message.text
    # Sabse pehle Anime/Movie search karein
    anime_url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    
    try:
        time.sleep(1) # API limit se bachne ke liye
        response = requests.get(anime_url)
        data = response.json().get('data', [])
        
        if data:
            item = data[0]
            title = item.get('title', 'N/A')
            rating = item.get('score', 'N/A')
            image_url = item.get('images', {}).get('jpg', {}).get('large_image_url')
            
            caption = f"🎬 **Name:** {title}\n⭐ **Rating:** {rating}"
            bot.send_photo(message.chat.id, image_url, caption=caption, parse_mode="Markdown")
        
        else:
            # Agar movie nahi mili, toh Character search karein
            char_url = f"https://api.jikan.moe/v4/characters?q={query}&limit=1"
            char_res = requests.get(char_url)
            char_data = char_res.json().get('data', [])
            
            if char_data:
                char = char_data[0]
                name = char.get('name', 'N/A')
                favs = char.get('favorites', 0)
                char_img = char.get('images', {}).get('jpg', {}).get('image_url')
                
                caption = f"👤 **Character:** {name}\n⭐ **Popularity:** {favs}"
                bot.send_photo(message.chat.id, char_img, caption=caption, parse_mode="Markdown")
            else:
                bot.reply_to(message, "❌ Dragon Ball world mein ye nahi mila. Sahi spelling likhein!")

    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "⚠️ Connection Error! Thodi der baad try karein.")

# Bot polling start karne ke liye
print("Master Bot v2 is running...")
bot.infinity_polling()
    
