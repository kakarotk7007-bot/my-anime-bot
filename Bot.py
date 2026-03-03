import os
import telebot
from telebot import types
from keep_alive import keep_alive

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

CHANNEL_NAME = "@dragonballsuperbeerus"
keep_alive()

# 🖼️ Posters Gallery
POSTERS = {
    "classic": "https://m.media-amazon.com/images/M/MV5BMjI0ZGY0YjctNTE5MS00MTY2LWI1ZDYtOTM5ZWZkZGU4MTM2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbz_kai": "https://m.media-amazon.com/images/M/MV5BMDE1MGRiNTgtZGE0Ny00ZDliLTk0N2ItYmU0NWRhY2VkY2M4XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbgt": "https://m.media-amazon.com/images/M/MV5BMWRiMGRhNjYtZGUxNC00ZTRjLWI0OTctY2Y0YmFmYjZkYWEyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbs": "https://wallpaperaccess.com/full/1510461.jpg",
    "daima": "https://m.media-amazon.com/images/M/MV5BZjY5N2VjZTAtNjA2Yi00N2VmLThhNzAtYmY3ZGRmYmFjZWRmXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_.jpg",
    "heroes": "https://i.pinimg.com/736x/01/75/a3/0175a3630f5b9d212711d59656209e74.jpg"
}

# 🐉 डेटाबेस (आपके फोटो वाले फॉर्मेट में)
DB_DATA = {
    "classic": (
        "🌟 **Dragon Ball**\n\n"
        "📅 **Released:** 1986–1989\n"
        "⭐ **Rating:** 8.4/10\n"
        "🎭 **Main Heroes:** Kid Goku, Bulma, Krillin\n\n"
        "📝 **History:** Gokuu Son is a young boy who lives in the woods all alone—that is, until a girl named Bulma runs into him in her search for a set of magical objects called the 'Dragon Balls.' Since the artifacts are said to grant one wish to whoever collects all seven, Bulma hopes to gather them and wish for a perfect boyfriend. Gokuu happens to be in possession of a 4-star ball..."
    ),
    "dbz_kai": (
        "🌟 **Dragon Ball Z Kai**\n\n"
        "📅 **Released:** 2009–2011; 2014–2015\n"
        "⭐ **Rating:** 8.2/10\n"
        "🎭 **Main Heroes:** Goku, Vegeta, Gohan\n\n"
        "📝 **History:** A remastered, faster-paced version of Dragon Ball Z with less filler, bringing it closer to the original manga. It follows adult Goku and his fight against new alien threats five years after the original series ended."
    ),
    "dbgt": (
        "🌟 **Dragon Ball GT (Non-Canon)**\n\n"
        "📅 **Released:** 1996–1997\n"
        "⭐ **Rating:** 6.8/10\n"
        "🎭 **Main Heroes:** SSJ4 Goku, Pan, Trunks\n\n"
        "📝 **History:** A 64-episode series that takes place after Dragon Ball Z. After a mistake with the Black Star Dragon Balls, Goku is turned back into a child. It is considered non-canon because it was not based on Akira Toriyama's manga."
    ),
    "dbs": (
        "🌟 **Dragon Ball Super**\n\n"
        "📅 **Released:** 2015–2018\n"
        "⭐ **Rating:** 8.3/10\n"
        "🎭 **Main Heroes:** Goku, Vegeta, Beerus\n\n"
        "📝 **History:** Set after the defeat of Majin Buu, it is considered official canon. Goku encounters divine powers, gods of destruction, and enters multiversal tournaments to protect Earth."
    ),
    "daima": (
        "🌟 **Dragon Ball Daima**\n\n"
        "📅 **Released:** 2024–2025\n"
        "⭐ **Rating:** 8.2/10\n"
        "🎭 **Main Heroes:** Kid Goku, Glorio, Shin\n\n"
        "📝 **History:** The newest series created to celebrate the 40th anniversary of the franchise. Due to a conspiracy, Goku and his friends are turned small and must head to the Demon Realm to fix things."
    ),
    "heroes": (
        "🌟 **Super Dragon Ball Heroes (Promo)**\n\n"
        "📅 **Released:** 2018–2024\n"
        "⭐ **Rating:** 7.0/10\n"
        "🎭 **Main Heroes:** CC Goku, Xeno Goku, Fu\n\n"
        "📝 **History:** A promotional anime series for the card game. It features non-canon 'dream battles' like Super Saiyan 4 vs. Super Saiyan Blue in various multiversal arcs."
    )
}

# 🔍 Aliases for smart searching
ALIASES = {
    "classic": "classic", "dragon ball": "classic",
    "dbz kai": "dbz_kai", "kai": "dbz_kai", "dragon ball z kai": "dbz_kai",
    "gt": "dbgt", "dragon ball gt": "dbgt",
    "super": "dbs", "dbs": "dbs", "dragon ball super": "dbs",
    "daima": "daima", "dragon ball daima": "daima",
    "heroes": "heroes", "sdbh": "heroes", "super dragon ball heroes": "heroes"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🐉 **Dragon Ball Hub Online!**\n\nकिसी भी सीरीज का नाम लिखें (जैसे: `DBZ Kai`, `Daima`, `GT`) जानकारी के लिए।")

@bot.message_handler(func=lambda message: True)
def handle_requests(message):
    user_input = message.text.lower().strip()
    
    if user_input in ALIASES:
        key = ALIASES[user_input]
        bot.send_photo(
            message.chat.id, 
            POSTERS[key], 
            caption=f"{DB_DATA[key]}\n\n🔗 {CHANNEL_NAME}",
            parse_mode="Markdown"
        )

if __name__ == "__main__":
    bot.polling(none_stop=True)
