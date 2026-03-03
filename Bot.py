import os
import telebot
from telebot import types
from keep_alive import keep_alive

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

CHANNEL_NAME = "@dragonballsuperbeerus"
keep_alive()

# 🖼️ फोटो गैलरी
IMAGES = {
    "classic": "https://m.media-amazon.com/images/M/MV5BMjI0ZGY0YjctNTE5MS00MTY2LWI1ZDYtOTM5ZWZkZGU4MTM2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbz": "https://wallpapercave.com/wp/wp6617385.jpg",
    "dbgt": "https://m.media-amazon.com/images/M/MV5BMWRiMGRhNjYtZGUxNC00ZTRjLWI0OTctY2Y0YmFmYjZkYWEyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "dbs": "https://wallpaperaccess.com/full/1510461.jpg",
    "movies": "https://w0.peakpx.com/wallpaper/794/410/HD-wallpaper-dragon-ball-z-movie-posters-dragon-ball-z-movies-posters.jpg",
    "2026": "https://i.pinimg.com/736x/82/3e/2d/823e2d677610492878d655f9e2b0a395.jpg"
}

# 🐉 डेटाबेस आपके फॉर्मेट में
DB_DATA = {
    "classic": (
        "🌟 **Dragon Ball (1986)**\n\n"
        "📝 **History:** Gokuu Son is a young boy who lives in the woods all alone—that is, until a girl named Bulma runs into him in her search for a set of magical objects called the 'Dragon Balls.' Since the artifacts are said to grant one wish to whoever collects all seven, Bulma hopes to gather them and wish for a perfect boyfriend. Gokuu happens to be in possession of a 4-star ball..."
    ),
    "dbz": (
        "🌟 **Dragon Ball Z**\n\n"
        "📝 **History:** Five years after the events of Dragon Ball, Gokuu is now a young adult and a father. His peaceful life is interrupted when a mysterious alien named Raditz arrives, claiming to be Gokuu's long-lost brother. He reveals that Gokuu is a member of a nearly extinct warrior race called the Saiyans..."
    ),
    "dbgt": (
        "🌟 **Dragon Ball GT**\n\n"
        "📝 **History:** Emperor Pilaf finally gets his hands on the Black Star Dragon Balls and accidentally wishes Gokuu back into a child. Gokuu, Trunks, and Pan must travel across the galaxy to find these balls and save Earth from destruction in this non-canon adventure."
    ),
    "dbs": (
        "🌟 **Dragon Ball Super**\n\n"
        "📝 **History:** After the defeat of Majin Buu, peace has returned to Earth. However, this peace is short-lived as Beerus, the God of Destruction, awakens from a long slumber. Gokuu must reach the level of a Super Saiyan God to protect the universe from this new threat."
    ),
    "movies": (
        "🌟 **Dragon Ball Movies Library**\n\n"
        "📝 **History:** The franchise includes 21+ films ranging from classic adventures like 'Curse of the Blood Rubies' to modern blockbusters like 'Dragon Ball Super: Super Hero'. These movies explore alternate timelines and legendary villains like Broly and Janemba."
    ),
    "2026": (
        "🌟 **Dragon Ball 2026 (Future Projects)**\n\n"
        "📝 **History:** As we celebrate the 40th anniversary, new projects like 'Beerus Project' and 'Galactic Era' are in development to expand the lore of the Gods and the Saiyan race beyond the known multiverse."
    )
}

# 🔍 कीवर्ड मैपिंग
ALIASES = {
    "dragon ball": "classic", "classic": "classic", "db": "classic",
    "dbz": "dbz", "dragon ball z": "dbz",
    "gt": "dbgt", "dragon ball gt": "dbgt",
    "dbs": "dbs", "super": "dbs", "dragon ball super": "dbs",
    "movie": "movies", "movies": "movies", "film": "movies",
    "2026": "2026", "future": "2026"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🐉 **Dragon Ball Encyclopedia**\n\nType any series name (e.g., `DBZ`, `DBS`, `Movies`) to get its history.")

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
        # किसी और एनीमे पर कोई जवाब नहीं (या एरर मैसेज)
        pass 

if __name__ == "__main__":
    bot.polling(none_stop=True)
