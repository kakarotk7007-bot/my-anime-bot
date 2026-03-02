import os
import telebot
from telebot import types
from keep_alive import keep_alive

# Token and Bot Setup
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

CHANNEL_NAME = "@dragonballsuperbeerus"
keep_alive()

# 🖼️ Photo Links
POSTERS = {
    "classic": "https://m.media-amazon.com/images/M/MV5BMjI0ZGY0YjctNTE5MS00MTY2LWI1ZDYtOTM5ZWZkZGU4MTM2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbz": "https://wallpapercave.com/wp/wp6617385.jpg",
    "dbs": "https://wallpaperaccess.com/full/1510461.jpg",
    "movies": "https://w0.peakpx.com/wallpaper/794/410/HD-wallpaper-dragon-ball-z-movie-posters-dragon-ball-z-movies-posters.jpg",
    "future": "https://i.pinimg.com/736x/82/3e/2d/823e2d677610492878d655f9e2b0a395.jpg"
}

# 🐉 Master Database
DB_DATA = {
    "classic": (
        "🐉 **DRAGON BALL CLASSIC (1986-1989)**\n"
        "⭐ **Rating:** 8.4/10\n"
        "🎭 **Heroes:** Kid Goku, Bulma, Krillin\n\n"
        "📜 **Full Seasons:**\n"
        "1. Emperor Pilaf Arc\n"
        "2. Red Ribbon Army Arc\n"
        "3. King Piccolo Arc\n"
        "4. Piccolo Jr. Arc\n"
        "🦹 **Main Villain:** King Piccolo"
    ),
    "dbz": (
        "⚡ **DRAGON BALL Z (1989-1996)**\n"
        "⭐ **Rating:** 8.8/10\n"
        "🎭 **Heroes:** Goku, Vegeta, Gohan, Piccolo\n\n"
        "📜 **Full Seasons:**\n"
        "1. Saiyan Saaga (Vegeta)\n"
        "2. Frieza Saaga (Frieza)\n"
        "3. Cell Saaga (Cell)\n"
        "4. Majin Buu Saaga (Kid Buu)\n"
        "🦹 **Iconic Villain:** Frieza"
    ),
    "dbs": (
        "🌌 **DRAGON BALL SUPER (2015-2018)**\n"
        "⭐ **Rating:** 8.3/10\n"
        "🎭 **Heroes:** Goku, Vegeta, Beerus, Whis\n\n"
        "📜 **Full Arcs:**\n"
        "1. Battle of Gods (Beerus)\n"
        "2. Goku Black Arc (Zamasu)\n"
        "3. Tournament of Power (Jiren)\n"
        "4. Moro Arc (Manga Only)\n"
        "🦹 **Strongest Opponent:** Jiren"
    ),
    "movies": (
        "🎬 **DRAGON BALL MOVIES LIST**\n"
        "⭐ **Overall Rating:** 7.5/10\n\n"
        "📜 **Top Movies & Villains:**\n"
        "• Fusion Reborn (Janemba)\n"
        "• Broly: The Legendary Saiyan\n"
        "• DBS: Broly (Golden Frieza)\n"
        "• DBS: Super Hero (Cell Max)\n"
        "• **2026 Special:** 40th Anniversary Movie"
    ),
    "2026": (
        "🔥 **PROJECT 2026 & FUTURE**\n"
        "1. **Beerus Project:** विनाश के देवता की अनसुनी कहानी।\n"
        "2. **Galactic Era:** नई एनीमे सीरीज।\n"
        "3. **Goku New Form:** 2026 के स्पेशल प्रोजेक्ट में नए अवतार।"
    )
}

# Mapping keywords to specific data
ALIASES = {
    "classic": "classic", "dragon ball": "classic", "db": "classic",
    "dbz": "dbz", "dragon ball z": "dbz",
    "dbs": "dbs", "dragon ball super": "dbs",
    "movie": "movies", "movies": "movies", "film": "movies",
    "2026": "2026", "future": "2026"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "🐉 **Dragon Ball Encyclopedia (1986-2026)**\n\n"
        "जानकारी के लिए नीचे दिए गए नाम लिखें:\n"
        "• `Classic` (Dragon Ball 1986)\n"
        "• `DBZ` (Dragon Ball Z)\n"
        "• `DBS` (Dragon Ball Super)\n"
        "• `Movies` (All Films)\n"
        "• `2026` (Upcoming Projects)"
    )
    bot.reply_to(message, text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_all_requests(message):
    user_input = message.text.lower().strip()
    
    # Check if keyword exists in our dictionary
    if user_input in ALIASES:
        key = ALIASES[user_input]
        poster_url = POSTERS.get(key, POSTERS["classic"])
        
        bot.send_photo(
            message.chat.id, 
            poster_url, 
            caption=f"{DB_DATA[key]}\n\n🔗 {CHANNEL_NAME}",
            parse_mode="Markdown"
        )
    else:
        # Strict Block for other topics
        bot.reply_to(message, "❌ **सिर्फ ड्रैगन बॉल!**\nलिखें: `Classic`, `DBZ`, `DBS`, `Movies` या `2026`।")

if __name__ == "__main__":
    bot.polling(none_stop=True)
