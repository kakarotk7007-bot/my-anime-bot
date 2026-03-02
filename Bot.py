
import os
import telebot
from telebot import types
import requests
import urllib.parse
from keep_alive import keep_alive

# Token fetched from Render Environment Variables
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# Your Channel Information
CHANNEL_URL = "https://t.me/dragonballsuperbeerus"
CHANNEL_NAME = "@dragonballsuperbeerus"

keep_alive()

# 1986-2026 Database
DB_FRANCHISE = {
    "history": (
        "⏳ **Dragon Ball Timeline (1986 - 2026):**\n\n"
        "• **Dragon Ball (1986):** The beginning of Goku's adventure.\n"
        "• **Dragon Ball Z (1989):** The era of Saiyans and legendary battles.\n"
        "• **Dragon Ball GT (1996):** The Grand Tour journey.\n"
        "• **Dragon Ball Super (2015):** Introduction of Gods and Multiverse.\n"
        "• **Dragon Ball Daima (2024):** A new mysterious journey.\n"
        "• **Beerus Project (2026):** The latest saga exploring the God of Destruction's origins!"
    ),
    "2026": (
        "🔥 **2026 Special Projects:**\n\n"
        "1. **DBS: Beerus Project:** Exclusive new story about Lord Beerus.\n"
        "2. **Galactic Era:** New Manga chapters & Anime expansion.\n"
        "3. **Game:** Budokai Tenkaichi 5 (Sparking! Evolution).\n"
        "4. **40th Anniversary:** Global celebration event & movie leaks."
    ),
    "beerus": (
        "🟣 **DBS: Beerus Project (2026):**\n\n"
        "यह प्रोजेक्ट बीरस के 'God of Destruction' बनने की अनसुनी कहानी बताता है। इसमें गोकू और वेजीटा बीरस के साथ मिलकर ब्रह्मांड के नए खतरों का सामना करते हैं।"
    )
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📢 Join Main Channel", url=CHANNEL_URL)
    btn2 = types.InlineKeyboardButton("🚀 2026 Projects", callback_data="2026_info")
    markup.add(btn1)
    markup.add(btn2)
    
    welcome_msg = (
        "👋 **Welcome to the Dragon Ball Universe (1986-2026)!**\n\n"
        "I can give you info on any Anime or the latest 2026 projects.\n\n"
        "**Try these keywords:**\n"
        "• `History` - Full DB Timeline\n"
        "• `Beerus Project` - 2026 Special\n"
        "• `2026` - New Series & Games"
    )
    bot.reply_to(message, welcome_msg, parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    query = message.text.lower()
    
    # Custom Keyword Responses
    if "history" in query or "timeline" in query:
        bot.reply_to(message, DB_FRANCHISE['history'])
    elif "2026" in query:
        bot.reply_to(message, DB_FRANCHISE['2026'])
    elif "beerus project" in query or "beerus" in query:
        bot.reply_to(message, DB_FRANCHISE['beerus'])
    else:
        # If not a keyword, search via Internet API
        search_from_web(message)

def search_from_web(message):
    query_encoded = urllib.parse.quote(message.text)
    api_url = f"https://api.jikan.moe/v4/anime?q={query_encoded}&limit=1"
    
    try:
        response = requests.get(api_url).json()
        if response.get('data') and len(response['data']) > 0:
            anime = response['data'][0]
            title = anime.get('title', 'N/A')
            synopsis = anime.get('synopsis', 'No details found.')[:350] + "..."
            img_url = anime['images']['jpg']['large_image_url']
            
            caption = f"🌟 **{title}**\n\n📝 **History:** {synopsis}\n\n🔗 {CHANNEL_NAME}"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("🚀 More Updates on Channel", url=CHANNEL_URL))
            bot.send_photo(message.chat.id, img_url, caption=caption, parse_mode="Markdown", reply_markup=markup)
        else:
            # Not Found Message
            error_msg = "❌ **Not Found!**\n\nTry searching for `Beerus Project` or check your spelling."
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("📢 Check Channel", url=CHANNEL_URL))
            bot.reply_to(message, error_msg, reply_markup=markup)
    except:
        bot.reply_to(message, "⚠️ System Busy. Try again later!")

if __name__ == "__main__":
    bot.polling(none_stop=True)
