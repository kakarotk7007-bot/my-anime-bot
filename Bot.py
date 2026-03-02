import os
import telebot
import requests
import urllib.parse
from telebot import types
from keep_alive import keep_alive

# Token will be fetched from Render's Environment Variables
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# Your Channel Link as a proper URL
CHANNEL_URL = "https://t.me/dragonballsuperbeerus"
CHANNEL_NAME = "@dragonballsuperbeerus"

keep_alive()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    # Adding buttons with proper URLs
    btn1 = types.InlineKeyboardButton("📢 Join Main Channel", url=CHANNEL_URL)
    btn2 = types.InlineKeyboardButton("🔥 2026 Projects", url=CHANNEL_URL) 
    markup.add(btn1)
    markup.add(btn2)
    
    welcome_text = (
        "👋 **Welcome to the Dragon Ball Universe!**\n\n"
        "I can provide complete history and details for any Anime.\n\n"
        "🆕 **2026 Special Updates:**\n"
        "• 'Dragon Ball: New Era' Project is Live!\n"
        "• 'Budokai Tenkaichi 5' Official Trailer out!\n\n"
        "To search, just type the Anime name (e.g., `Dragon Ball Z`)."
    )
    bot.reply_to(message, welcome_text, parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def search_anime(message):
    query = message.text
    query_encoded = urllib.parse.quote(query)
    url = f"https://api.jikan.moe/v4/anime?q={query_encoded}&limit=1"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['data']:
            anime = data['data'][0]
            anime_id = anime['mal_id']
            img = anime['images']['jpg']['large_image_url']
            
            title = anime.get('title', 'N/A')
            score = anime.get('score', 'N/A')
            aired = anime.get('aired', {}).get('string', 'N/A')
            episodes = anime.get('episodes', 'N/A')
            status = anime.get('status', 'N/A')
            
            # Synopsis / History
            synopsis = anime.get('synopsis', 'No description available.')
            if synopsis: synopsis = synopsis[:350] + "..."
            
            # Fetch Main Character
            char_url = f"https://api.jikan.moe/v4/anime/{anime_id}/characters"
            char_res = requests.get(char_url).json()
            hero_name = "N/A"
            if char_res.get('data'):
                hero_name = char_res['data'][0]['character']['name']

            caption = (
                f"🌟 **Title:** {title}\n"
                f"🦸 **Main Hero:** {hero_name}\n"
                f"📅 **Aired:** {aired}\n"
                f"📊 **Rating:** {score}/10\n"
                f"📺 **Episodes:** {episodes}\n"
                f"📡 **Status:** {status}\n\n"
                f"📝 **History/Plot:** {synopsis}\n\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"🚀 **2026 Update:** Links available on our channel!\n"
                f"🔗 {CHANNEL_NAME}"
            )
            
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("🚀 Join Channel", url=CHANNEL_URL))
            
            bot.send_photo(message.chat.id, img, caption=caption, parse_mode="Markdown", reply_markup=markup)
        else:
            bot.reply_to(message, "Sorry, Anime not found!")
    except Exception:
        bot.reply_to(message, "⚠️ Server busy, please try again.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
        
