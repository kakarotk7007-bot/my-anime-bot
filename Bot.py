import os
import telebot
from telebot import types
from keep_alive import keep_alive

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# आपका चैनल लिंक
CHANNEL_NAME = "@dragonballsuperbeerus"
keep_alive()

# 🖼️ HD Official Posters (Tested Links)
IMAGES = {
    "classic": "https://m.media-amazon.com/images/M/MV5BMjI0ZGY0YjctNTE5MS00MTY2LWI1ZDYtOTM5ZWZkZGU4MTM2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbz_kai": "https://m.media-amazon.com/images/M/MV5BMDE1MGRiNTgtZGE0Ny00ZDliLTk0N2ItYmU0NWRhY2VkY2M4XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbgt": "https://m.media-amazon.com/images/M/MV5BMWRiMGRhNjYtZGUxNC00ZTRjLWI0OTctY2Y0YmFmYjZkYWEyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbs": "https://m.media-amazon.com/images/M/MV5BY2I2MzYxMTYtYzJkZC00MTBmLTllM2EtZDQ3Njg4N2RjNWUxXkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_.jpg",
    "daima": "https://m.media-amazon.com/images/M/MV5BZjY5N2VjZTAtNjA2Yi00N2VmLThhNzAtYmY3ZGRmYmFjZWRmXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_.jpg",
    "movies": "https://m.media-amazon.com/images/M/MV5BMjA2NTI2Njg3N15BMl5BanBnXkFtZTcwNTE4NzI4Mg@@._V1_.jpg",
    "heroes": "https://m.media-amazon.com/images/M/MV5BMTYxOTI5MDYtMGVjZi00YmY5LWI2NDUtZGU1Y2NlY2I2YmE3XkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_.jpg"
}

# 🐉 Full HD Details (Rating + Year + History)
DB_DATA = {
    "classic": (
        "🌟 **Dragon Ball (Classic)**\n\n"
        "📅 **Year:** 1986–1989\n"
        "⭐ **Rating:** 8.4/10\n\n"
        "📝 **History:** Gokuu Son is a young boy who lives in the woods all alone—until a girl named Bulma runs into him. They search for 'Dragon Balls' which grant a wish to whoever collects all seven."
    ),
    "dbz_kai": (
        "🌟 **Dragon Ball Z Kai**\n\n"
        "📅 **Year:** 2009–2015\n"
        "⭐ **Rating:** 8.2/10\n\n"
        "📝 **History:** A remastered, HD version of DBZ with less filler. It follows adult Goku's fight against alien threats like Frieza, Cell, and Majin Buu."
    ),
    "dbgt": (
        "🌟 **Dragon Ball GT**\n\n"
        "📅 **Year:** 1996–1997\n"
        "⭐ **Rating:** 6.8/10\n\n"
        "📝 **History:** Set after DBZ. Goku is turned back into a child by the Black Star Dragon Balls and travels across the galaxy to save Earth."
    ),
    "dbs": (
        "🌟 **Dragon Ball Super**\n\n"
        "📅 **Year:** 2015–2018\n"
        "⭐ **Rating:** 8.3/10\n\n"
        "📝 **History:** Official canon set after Buu's defeat. Goku encounters Beerus, the Multiverse, and achieves divine forms like Ultra Instinct."
    ),
    "daima": (
        "🌟 **Dragon Ball Daima**\n\n"
        "📅 **Year:** 2024–2025\n"
        "⭐ **Rating:** 8.2/10\n\n"
        "📝 **History:** Newest 40th-anniversary series. Goku and friends are turned small and must head to the Demon Realm."
    ),
    "movies": (
        "🌟 **Dragon Ball Movies**\n\n"
        "📅 **Count:** 21+ HD Films\n"
        "⭐ **Top Movie:** DB Super: Broly (8.0/10)\n\n"
        "📝 **History:** Side stories and official sequels (like Broly and Super Hero) that show the ultimate Saiyan battles."
    ),
    "heroes": (
        "🌟 **Dragon Ball Heroes**\n\n"
        "📅 **Year:** 2018–2024\n"
        "⭐ **Rating:** 7.0/10\n\n"
        "📝 **History:** Promotional anime with non-canon dream matches like SSJ4 vs SSJ Blue."
    )
}

# 🔍 HD Searching (Aliases)
ALIASES = {
    "dragon ball classic": "classic", "dragon ball": "classic", "classic": "classic",
    "dragon ball z kai": "dbz_kai", "dbz kai": "dbz_kai", "kai": "dbz_kai",
    "dragon ball gt": "dbgt", "gt": "dbgt",
    "dragon ball super": "dbs", "dbs": "dbs", "super": "dbs",
    "dragon ball daima": "daima", "daima": "daima",
    "movies": "movies", "movie": "movies", "film": "movies",
    "heroes": "heroes", "sdbh": "heroes"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🐉 **HD Dragon Ball Encyclopedia**\n\nType any name (e.g., `Dragon Ball`, `Super`, `Movies`) for HD details!")

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
        bot.reply_to(message, "❌ **HD Data not found!**\nTry: `Dragon Ball`, `Super`, `Movies`.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
