import os
import telebot
from telebot import types
from keep_alive import keep_alive

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# आपका चैनल लिंक
CHANNEL_NAME = "@dragonballsuperbeerus"
keep_alive()

# 🖼️ बिल्कुल सही एनीमे पोस्टर्स के लिंक्स
IMAGES = {
    "classic": "https://m.media-amazon.com/images/M/MV5BMjI0ZGY0YjctNTE5MS00MTY2LWI1ZDYtOTM5ZWZkZGU4MTM2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbz_kai": "https://m.media-amazon.com/images/M/MV5BMDE1MGRiNTgtZGE0Ny00ZDliLTk0N2ItYmU0NWRhY2VkY2M4XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbgt": "https://m.media-amazon.com/images/M/MV5BMWRiMGRhNjYtZGUxNC00ZTRjLWI0OTctY2Y0YmFmYjZkYWEyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbs": "https://m.media-amazon.com/images/M/MV5BY2I2MzYxMTYtYzJkZC00MTBmLTllM2EtZDQ3Njg4N2RjNWUxXkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_.jpg",
    "daima": "https://m.media-amazon.com/images/M/MV5BZjY5N2VjZTAtNjA2Yi00N2VmLThhNzAtYmY3ZGRmYmFjZWRmXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_.jpg",
    "heroes": "https://m.media-amazon.com/images/M/MV5BMTYxOTI5MDYtMGVjZi00YmY5LWI2NDUtZGU1Y2NlY2I2YmE3XkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_FMjpg_UX1000_.jpg"
}

# 🐉 सभी एनीमे की पूरी डिटेल्स
DB_DATA = {
    "classic": (
        "🌟 **Dragon Ball (Classic)**\n\n"
        "📅 Released: 1986–1989\n"
        "⭐ Rating: 8.4/10\n\n"
        "📝 History: Gokuu Son is a young boy who lives in the woods all alone—that is, until a girl named Bulma runs into him in her search for a set of magical objects called the 'Dragon Balls'..."
    ),
    "dbz_kai": (
        "🌟 **Dragon Ball Z Kai**\n\n"
        "📅 Released: 2009–2015\n"
        "⭐ Rating: 8.2/10\n\n"
        "📝 History: A remastered, faster-paced version of Dragon Ball Z with less filler, bringing it closer to the original manga. It follows Goku's fight against powerful threats like Frieza, Cell, and Buu."
    ),
    "dbgt": (
        "🌟 **Dragon Ball GT**\n\n"
        "📅 Released: 1996–1997\n"
        "⭐ Rating: 6.8/10\n\n"
        "📝 History: Takes place after Dragon Ball Z. After a mistake with the Black Star Dragon Balls, Goku is turned back into a child and must travel across the galaxy."
    ),
    "dbs": (
        "🌟 **Dragon Ball Super**\n\n"
        "📅 Released: 2015–2018\n"
        "⭐ Rating: 8.3/10\n\n"
        "📝 History: Set after the defeat of Majin Buu, it is official canon. Goku encounters divine powers, gods of destruction like Beerus, and enters multiversal tournaments."
    ),
    "daima": (
        "🌟 **Dragon Ball Daima**\n\n"
        "📅 Released: 2024–2025\n"
        "⭐ Rating: 8.2/10\n\n"
        "📝 History: The newest series created for the 40th anniversary. Goku and his friends are turned small and head to the Demon Realm to fix a mysterious conspiracy."
    ),
    "heroes": (
        "🌟 **Super Dragon Ball Heroes**\n\n"
        "📅 Released: 2018–2024\n"
        "⭐ Rating: 7.0/10\n\n"
        "📝 History: A promotional anime series featuring non-canon 'dream battles' like Super Saiyan 4 vs. Super Saiyan Blue in various multiversal arcs."
    )
}

# 🔍 Aliases: ताकि "Dragon Ball classic" जैसे नाम भी काम करें
ALIASES = {
    "dragon ball classic": "classic", "classic": "classic", "dragon ball": "classic",
    "dragon ball z kai": "dbz_kai", "dbz kai": "dbz_kai", "kai": "dbz_kai",
    "dragon ball gt": "dbgt", "gt": "dbgt",
    "dragon ball super": "dbs", "dbs": "dbs", "super": "dbs",
    "dragon ball daima": "daima", "daima": "daima",
    "super dragon ball heroes": "heroes", "heroes": "heroes", "sdbh": "heroes"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🐉 **Dragon Ball Encyclopedia**\n\nType any series name (e.g., `Dragon Ball classic`, `DBZ Kai`, `Daima`) to get full details with official poster!")

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
        bot.reply_to(message, "❌ **Data not found!**\nTry typing: `Dragon Ball classic`, `DBZ Kai`, `GT`, `Super`, or `Daima`.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
