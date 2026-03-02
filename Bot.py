import os
import telebot
from telebot import types
from keep_alive import keep_alive

# Token from Render Env Var
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

CHANNEL_URL = "https://t.me/dragonballsuperbeerus"
CHANNEL_NAME = "@dragonballsuperbeerus"

keep_alive()

# 🐉 Pure Dragon Ball Database (1986-2026)
# यहाँ सिर्फ वही शब्द हैं जिनका जवाब बोट देगा
DB_DATA = {
    "1986": "🐉 **Dragon Ball (1986):**\nयह वह शुरुआत है जहाँ नन्हे गोकू और बुलमा पहली बार ड्रैगन बॉल्स की खोज पर निकलते हैं।",
    "1989": "⚡ **Dragon Ball Z (1989):**\nसैयां सागा से लेकर माजिन बू तक की महान लड़ाईयाँ। इसमें गोकू पहली बार सुपर सैयां बना था।",
    "2015": "🌌 **Dragon Ball Super (2015):**\nविनाश के देवता बीरस का आगमन और मल्टीवर्स का टूर्नामेंट।",
    "2024": "🧒 **Dragon Ball Daima (2024):**\nएक नई कहानी जहाँ गोकू और उसके साथी फिर से छोटे हो जाते हैं।",
    "2026": "🔥 **2026 Projects:**\n1. **Beerus Project:** बीरस की उत्पत्ति की कहानी।\n2. **Galactic Era:** नई एनीमे सीरीज।\n3. **40th Anniversary:** स्पेशल मूवी और इवेंट्स।",
    "beerus": "🟣 **Lord Beerus:**\nयूनिवर्स 7 के विनाश के देवता। 2026 में इनका 'Beerus Project' सबसे बड़ा आकर्षण है।",
    "goku": "⭐ **Son Goku:**\nपृथ्वी का सबसे शक्तिशाली योद्धा। 2026 में गोकू के नए 'Divine Forms' देखने को मिलेंगे।",
    "history": "⏳ **Dragon Ball Timeline:**\n1986 ➔ 1989 ➔ 1996 (GT) ➔ 2015 ➔ 2024 ➔ 2026",
    "vegeta": "👑 **Prince Vegeta:**\nसैयां का गौरव। अल्ट्रा ईगो और 2026 की नई ट्रेनिंग के साथ वापस आ रहा है।",
    "broly": "🟢 **Legendary Broly:**\nअसीमित शक्ति वाला सैयां। 2026 के प्रोजेक्ट्स में ब्रोली की अहम भूमिका होगी।"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📢 Join DB Channel", url=CHANNEL_URL))
    
    text = (
        "🐉 **Welcome to the Pure Dragon Ball Universe!**\n\n"
        "मैं सिर्फ ड्रैगन बॉल (1986-2026) का एक्सपर्ट हूँ।\n"
        "जानकारी के लिए नीचे दिए गए शब्दों में से कोई **एक** लिखें:\n\n"
        "• `1986`, `1989`, `2015`, `2024`, `2026`\n"
        "• `History`, `Goku`, `Beerus`, `Vegeta`, `Broly`"
    )
    bot.reply_to(message, text, parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_db_only(message):
    # User के मैसेज को साफ करना (स्पेस हटाना और छोटे अक्षरों में करना)
    user_input = message.text.lower().strip()
    
    # अगर यूजर का इनपुट हमारे DB में है
    if user_input in DB_DATA:
        response = f"{DB_DATA[user_input]}\n\n🔗 {CHANNEL_NAME}"
        bot.reply_to(message, response, parse_mode="Markdown")
    else:
        # अगर यूजर कुछ और लिखता है (जैसे 'Hi', 'Naruto', या कुछ भी फालतू)
        error_msg = (
            "❌ **सिर्फ ड्रैगन बॉल!**\n\n"
            "मैं और किसी चीज़ का जवाब नहीं देता। कृपया सही नाम लिखें जैसे: `Goku` या `2026`।"
        )
        bot.reply_to(message, error_msg)

if __name__ == "__main__":
    bot.polling(none_stop=True)
