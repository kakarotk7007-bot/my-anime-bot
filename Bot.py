import telebot
import requests
import os

# Render ke Environment Variables se token uthane ke liye
# Wahan Key mein 'BOT_TOKEN' likhna zaruri hai
API_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = (
        "🔥 **Dragon Ball Encyclopedia Bot**\n\n"
        "Series, Movie ya Character ka naam likho:\n"
        "• Dragon Ball Z\n"
        "• Dragon Ball Super\n"
        "• Son Goku"
    )
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def search_dragon_ball(message):
    query = message.text
    anime_url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"
    
    try:
        response = requests.get(anime_url)
        data = response.json().get('data', [])
        
        if data:
            result = data[0]
            title = result.get('title')
            rating = result.get('score', 'N/A')
            image_url = result['images']['jpg']['large_image_url']
            media_type = result.get('type', 'N/A')

            caption = (f"🎬 **Name:** {title}\n"
                       f"⭐ **Rating:** {rating}\n"
                       f"📌 **Type:** {media_type}")
            
            bot.send_photo(message.chat.id, image_url, caption=caption, parse_mode="Markdown")
        else:
            char_url = f"https://api.jikan.moe/v4/characters?q={query}&limit=1"
            char_res = requests.get(char_url)
            char_data = char_res.json().get('data', [])
            
            if char_data:
                char = char_data[0]
                name = char['name']
                favs = char.get('favorites', 0)
                char_img = char['images']['jpg']['image_url']

                caption = (f"👤 **Hero Name:** {name}\n"
                           f"⭐ **Popularity:** {favs}")
                
                bot.send_photo(message.chat.id, char_img, caption=caption, parse_mode="Markdown")
            else:
                bot.reply_to(message, "❌ Dragon Ball world mein ye nahi mila.")
                
    except Exception:
        bot.reply_to(message, "⚠️ Connection Error!")

bot.infinity_polling()
