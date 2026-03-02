import os
import telebot
from telebot import types
from keep_alive import keep_alive

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

CHANNEL_URL = "https://t.me/dragonballsuperbeerus"
CHANNEL_NAME = "@dragonballsuperbeerus"

keep_alive()

# 🐉 केवल ड्रैगन बॉल का डेटाबेस (1986-2026)
DB_DATA = {
    "all": "📜 **Dragon Ball Series (1986-2026):**\n• DB (1986)\n• DBZ (1989)\n• DB GT (1996)\n• DB Kai (2009)\n• DBS (2015)\n• DB Daima (2024)\n• **Beerus Project (2026)**",
    "movies": "🎬 **Dragon Ball Movies:**\nइसमें 1986 से 2026 तक की सभी 22 फिल्में शामिल हैं। पूरी लिस्ट के लिए 'Movies' टाइप करें।",
    "2026": "🔥 **2026 New Era:** बीरस प्रोजेक्ट और 40th Anniversary मूवी आ रही है।",
    "goku": "⭐ **Son Goku:** ब्रह्मांड का सबसे शक्तिशाली योद्धा (1986-2026)।",
    "beerus": "🟣 **Lord Beerus:** विनाश के देवता। 2026 के नए प्रोजेक्ट के मुख्य पात्र।",
    "history": "⏳ **Timeline:** 1986 ➔ 1989 ➔ 1996 ➔ 2015 ➔ 2024 ➔ 2026",
    "vegeta": "👑 **Prince Vegeta:** सैयां राजकुमार और गोकू का प्रतिद्वंद्वी।",
    "broly": "🟢 **Legendary Broly:** असीमित शक्ति वाला सैयां।"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📢 Join DB Channel", url=CHANNEL_URL))
    
    text = (
        "🐉 **Welcome to Dragon Ball ONLY Bot!**\n\n"
        "मैं सिर्फ ड्रैगन बॉल (1986-2026) के बारे में जानता हूँ।\n"
        "किसी और एनीमे की जानकारी यहाँ नहीं मिलेगी।\n\n"
        "**इनमें से कुछ लिखें:**\n"
        "`All`, `Movies`, `2026`, `Goku`, `Beerus`, `History`"
    )
    bot.reply_to(message, text, parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_strict_db(message):
    # यूज़र के मैसेज को चेक करना
    user_input = message.text.lower().strip()
    
    # अगर शब्द ड्रैगन बॉल डेटाबेस में है
    if user_input in DB_DATA:
        bot.reply_to(message, f"{DB_DATA[user_input]}\n\n🔗 {CHANNEL_NAME}", parse_mode="Markdown")
    else:
        # अगर कोई और एनीमे या कुछ और सर्च करे, तो यह मैसेज जाएगा
        error_msg = (
            "❌ **Error: Not a Dragon Ball Topic!**\n\n"
            "मैं सिर्फ **Dragon Ball** का एक्सपर्ट हूँ।\n"
            "मैं किसी और एनीमे (जैसे Naruto, One Piece आदि) का जवाब नहीं देता।\n\n"
            "कृपया सिर्फ ड्रैगन बॉल से जुड़ा शब्द लिखें।"
        )
        bot.reply_to(message, error_msg)

if __name__ == "__main__":
    bot.polling(none_stop=True)
