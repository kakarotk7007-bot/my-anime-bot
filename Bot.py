import os
import telebot
from telebot import types
from keep_alive import keep_alive

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# आपका चैनल लिंक
CHANNEL_NAME = "@dragonballsuperbeerus"
keep_alive()

# 🖼️ High-Quality Official Anime Posters
# इन लिंक्स को मैंने टेस्ट किया है, ये टेलीग्राम पर एकदम सही फोटो दिखाएंगे।
IMAGES = {
    "classic": "https://m.media-amazon.com/images/M/MV5BMjI0ZGY0YjctNTE5MS00MTY2LWI1ZDYtOTM5ZWZkZGU4MTM2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg",
    "dbz_kai": "https://m.media-amazon.com/images/M/MV5BMDE1MGRiNTgtZGE0Ny00ZDliLTk0N2ItYmU0NWRhY2VkY2M4XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg",
    "dbgt": "https://m.media-amazon.com/images/M/MV5BMWRiMGRhNjYtZGUxNC00ZTRjLWI0OTctY2Y0YmFmYjZkYWEyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg",
    "dbs": "https://m.media-amazon.com/images/M/MV5BY2I2MzYxMTYtYzJkZC00MTBmLTllM2EtZDQ3Njg4N2RjNWUxXkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_FMjpg_UX1000_.jpg",
    "daima": "https://m.media-amazon.com/images/M/MV5BZjY5N2VjZTAtNjA2Yi00N2VmLThhNzAtYmY3ZGRmYmFjZWRmXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_FMjpg_UX1000_.jpg",
    "heroes": "https://m.media-amazon.com/images/M/MV5BMTYxOTI5MDYtMGVjZi00YmY5LWI2NDUtZGU1Y2NlY2I2YmE3XkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_FMjpg_UX1000_.jpg"
}

# 🐉 सभी एनीमे की पूरी डिटेल्स (Rating, Year, History)
DB_DATA = {
    "classic": (
        "🌟 **Dragon Ball (Classic)**\n\n"
        "📅 **Released:** 1986–1989\n"
        "⭐ **Rating:** 8.4/10\n\n"
        "📝 **History:** Gokuu Son is a young boy who lives in the woods all alone—until a girl named Bulma runs into him. They search for 'Dragon Balls' which grant a wish to whoever collects all seven."
    ),
    "dbz_kai": (
        "🌟 **Dragon Ball Z Kai**\n\n"
        "📅 **Released:** 2009–2015\n"
        "⭐ **Rating:** 8.2/10\n\n"
        "📝 **History:** A remastered version of Dragon Ball Z with less filler. It follows adult Goku and his fight against new alien threats and villains like Frieza, Cell, and Buu."
    ),
    "dbgt": (
        "🌟 **Dragon Ball GT**\n\n"
        "📅 **Released:** 1996–1997\n"
        "⭐ **Rating:** 6.8/10\n\n"
        "📝 **History:** Set after DBZ, Goku is turned back into a child by the Black Star Dragon Balls. He must travel across the galaxy to find them and save Earth."
    ),
    "dbs": (
        "🌟 **Dragon Ball Super**\n\n"
        "📅 **Released:** 2015–2018\n"
        "⭐ **Rating:** 8.3/10\n\n"
        "📝 **History:** Picking up after Majin Buu's defeat, Goku encounters gods of destruction like Beerus and divine powers. It is official canon."
    ),
    "daima": (
        "🌟 **Dragon Ball Daima**\n\n"
        "📅 **Released:** 2024–2025\n"
        "⭐ **Rating:** 8.2/10\n\n"
        "📝 **History:** The newest series for the 40th anniversary. Goku and his friends are turned small and must head to the Demon Realm to solve a mystery."
    ),
    "heroes": (
        "🌟 **Super Dragon Ball Heroes**\n\n"
        "📅 **Released:** 2018–2024\n"
        "⭐ **Rating:** 7.0/10\n\n"
        "📝 **History:** A promotional anime series featuring non-canon battles like Super Saiyan 4 vs. Super Saiyan Blue in various multiversal arcs."
    )
}

# 🔍 Aliases: ताकि यूजर 'Dragon Ball' लिखे या 'Classic', बोट समझ जाए
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
    bot.reply_to(message, "🐉 **Dragon Ball Encyclopedia**\n\nकिसी भी सीरीज का नाम लिखें (जैसे: `Dragon Ball classic`, `DBZ Kai`, `Daima`) जानकारी के लिए।")

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
