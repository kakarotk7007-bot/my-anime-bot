import os
import telebot
from telebot import types
from keep_alive import keep_alive

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# आपका चैनल लिंक
CHANNEL_NAME = "@dragonballsuperbeerus"
keep_alive()

# 🖼️ High-Quality Official Posters
IMAGES = {
    "classic": "https://m.media-amazon.com/images/M/MV5BMjI0ZGY0YjctNTE5MS00MTY2LWI1ZDYtOTM5ZWZkZGU4MTM2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbz_kai": "https://m.media-amazon.com/images/M/MV5BMDE1MGRiNTgtZGE0Ny00ZDliLTk0N2ItYmU0NWRhY2VkY2M4XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbgt": "https://m.media-amazon.com/images/M/MV5BMWRiMGRhNjYtZGUxNC00ZTRjLWI0OTctY2Y0YmFmYjZkYWEyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbs": "https://m.media-amazon.com/images/M/MV5BY2I2MzYxMTYtYzJkZC00MTBmLTllM2EtZDQ3Njg4N2RjNWUxXkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_.jpg",
    "daima": "https://m.media-amazon.com/images/M/MV5BZjY5N2VjZTAtNjA2Yi00N2VmLThhNzAtYmY3ZGRmYmFjZWRmXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_.jpg",
    "movies": "https://m.media-amazon.com/images/M/MV5BMjA2NTI2Njg3N15BMl5BanBnXkFtZTcwNTE4NzI4Mg@@._V1_.jpg"
}

# 🐉 प्रॉपर डिटेल्स (Movies Included)
DB_DATA = {
    "classic": (
        "🌟 **Dragon Ball (Classic)**\n\n"
        "📅 **Released:** 1986–1989\n"
        "⭐ **Rating:** 8.4/10\n\n"
        "📝 **History:** Gokuu Son is a young boy who lives in the woods all alone—until a girl named Bulma runs into him. Together they search for the 'Dragon Balls' to grant a wish."
    ),
    "dbz_kai": (
        "🌟 **Dragon Ball Z Kai**\n\n"
        "📅 **Released:** 2009–2015\n"
        "⭐ **Rating:** 8.2/10\n\n"
        "📝 **History:** A remastered version of Dragon Ball Z with less filler. It follows adult Goku and his fight against Frieza, Cell, and Majin Buu."
    ),
    "dbs": (
        "🌟 **Dragon Ball Super**\n\n"
        "📅 **Released:** 2015–2018\n"
        "⭐ **Rating:** 8.3/10\n\n"
        "📝 **History:** Official canon set after Majin Buu's defeat. Introduces Beerus, the Multiverse, and Ultra Instinct."
    ),
    "movies": (
        "🌟 **Dragon Ball Movies**\n\n"
        "📅 **Count:** 21+ Films\n"
        "⭐ **Top Movie:** DB Super: Broly (8.0/10)\n\n"
        "📝 **History:** The franchise has many films, from 'Dead Zone' to 'Super Hero'. Most are side-stories, while others like 'Broly' and 'Super Hero' are official parts of the timeline."
    )
}

# 🔍 Aliases (New movies alias added)
ALIASES = {
    "dragon ball": "classic", "classic": "classic", "dragon ball classic": "classic",
    "dbz kai": "dbz_kai", "kai": "dbz_kai", "dragon ball z kai": "dbz_kai",
    "dbgt": "dbgt", "gt": "dbgt",
    "dbs": "dbs", "super": "dbs", "dragon ball super": "dbs",
    "daima": "daima", "dragon ball daima": "daima",
    "movies": "movies", "movie": "movies", "film": "movies"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🐉 **Dragon Ball Encyclopedia**\n\nType any name (e.g., `Dragon Ball`, `Super`, `Movies`) to get details!")

@bot.message_handler(func=lambda message: True)
def handle_requests(message):
    user_input = message.text.lower().strip()
    
    if user_input in ALIASES:
        key = ALIASES[user_input]
        bot.send_photo(
            message.chat.id, 
            IMAGES[key], 
            caption=f"{DB_DATA[key]}\n\n🔗 {CHANNEL_NAME}",
            parse_mode="Markdown"
        )
    else:
        bot.reply_to(message, "❌ **Data not found!**\nTry: `Dragon Ball`, `Super`, `Movies`.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
