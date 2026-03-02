import os
import telebot
from telebot import types
from keep_alive import keep_alive

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

CHANNEL_NAME = "@dragonballsuperbeerus"
keep_alive()

# 🐉 Master Database: Series & Movies
DB_DATA = {
    "dbz": (
        "⚡ **DRAGON BALL Z (1989-1996)**\n"
        "⭐ **Rating:** 8.8/10\n\n"
        "📜 **Seasons & Villains:**\n"
        "• Saiyan Arc (Vegeta)\n"
        "• Frieza Arc (Frieza)\n"
        "• Cell Arc (Cell)\n"
        "• Buu Arc (Kid Buu)\n"
        "🎭 **Heroes:** Goku, Vegeta, Gohan"
    ),
    "dbs": (
        "🌌 **DRAGON BALL SUPER (2015-2018)**\n"
        "⭐ **Rating:** 8.3/10\n\n"
        "📜 **Arcs & Villains:**\n"
        "• Battle of Gods (Beerus)\n"
        "• Goku Black Arc (Zamasu)\n"
        "• Tournament of Power (Jiren)\n"
        "• Moro Arc (Manga Villain)\n"
        "🎭 **Heroes:** Goku, Vegeta, Whis"
    ),
    "movies": (
        "🎬 **DRAGON BALL ALL MOVIES LIST**\n\n"
        "**Classic Movies:**\n"
        "1. Curse of the Blood Rubies (Villain: Gurumes)\n"
        "2. Mystical Adventure (Villain: Tao Pai Pai)\n\n"
        "**DBZ Mega Hits:**\n"
        "3. Cooler's Revenge (Villain: Cooler) ⭐ 7.2/10\n"
        "4. Broly – The Legendary Super Saiyan ⭐ 7.5/10\n"
        "5. Fusion Reborn (Villain: Janemba) ⭐ 7.7/10\n"
        "6. Wrath of the Dragon (Villain: Hirudegarn)\n\n"
        "**Modern Blockbusters:**\n"
        "7. DBS: Broly (2018) ⭐ 7.9/10\n"
        "8. DBS: Super Hero (2022) ⭐ 7.1/10\n"
        "9. **2026 Special:** 40th Anniversary Movie (Coming Soon)"
    ),
    "2026": (
        "🔥 **2026 PROJECTS**\n"
        "• **Beerus Project:** विनाश के देवता की अनसुनी कहानी।\n"
        "• **Galactic Era:** नई एनीमे सीरीज और विलेन्स।\n"
        "• **Movie 2026:** ड्रैगन बॉल की 40वीं सालगिरह की मेगा फिल्म।"
    )
}

# Alias Mapping
ALIASES = {
    "movie": "movies",
    "films": "movies",
    "dragon ball z": "dbz",
    "dragon ball super": "dbs",
    "dragon ball": "dbz"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "🐉 **Dragon Ball Hub (1986-2026)**\n\n"
        "जानकारी के लिए नीचे दिए गए शब्द लिखें:\n"
        "• `Movies` - सभी फिल्मों के लिए\n"
        "• `DBZ` - ड्रैगन बॉल जेड के लिए\n"
        "• `DBS` - ड्रैगन बॉल सुपर के लिए\n"
        "• `2026` - नए प्रोजेक्ट्स के लिए"
    )
    bot.reply_to(message, text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    user_input = message.text.lower().strip()
    target_key = ALIASES.get(user_input, user_input)
    
    if target_key in DB_DATA:
        response = f"{DB_DATA[target_key]}\n\n🔗 {CHANNEL_NAME}"
        bot.reply_to(message, response, parse_mode="Markdown")
    else:
        bot.reply_to(message, "❌ **सिर्फ ड्रैगन बॉल!**\nलिखें: `Movies`, `DBZ` या `2026`।")

if __name__ == "__main__":
    bot.polling(none_stop=True)
