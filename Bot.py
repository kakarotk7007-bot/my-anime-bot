import os
import telebot
from telebot import types
from keep_alive import keep_alive

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

CHANNEL_NAME = "@dragonballsuperbeerus"
keep_alive()

# 🐉 Detailed Database: Rating, Heroes & Year
DB_DATA = {
    "1986": "🐉 **Dragon Ball (Classic)**\n📅 **Year:** 1986-1989\n⭐ **Rating:** 8.4/10\n🎭 **Heroes:** Goku, Bulma, Krillin, Master Roshi\n📝 **Story:** गोकू का बचपन और ड्रैगन बॉल्स की पहली खोज।",
    
    "1989": "⚡ **Dragon Ball Z**\n📅 **Year:** 1989-1996\n⭐ **Rating:** 8.8/10\n🎭 **Heroes:** Goku, Vegeta, Gohan, Piccolo\n📝 **Story:** सैयां सागा से लेकर माजिन बू तक की महान लड़ाईयाँ।",
    
    "2015": "🌌 **Dragon Ball Super**\n📅 **Year:** 2015-2018\n⭐ **Rating:** 8.3/10\n🎭 **Heroes:** Goku, Vegeta, Beerus, Whis\n📝 **Story:** विनाश के देवता बीरस और टूर्नामेंट ऑफ पावर।",
    
    "2024": "🧒 **Dragon Ball Daima**\n📅 **Year:** 2024\n⭐ **Rating:** 8.2/10 (Initial)\n🎭 **Heroes:** Mini Goku, Kaioshin, Glorio\n📝 **Story:** गोकू का नया एडवेंचर जहाँ सब छोटे हो गए हैं।",
    
    "2026": "🔥 **Beerus Project (Upcoming)**\n📅 **Year:** 2026\n⭐ **Rating:** Expected 9.0+\n🎭 **Heroes:** Beerus, Oracle Fish, Past Gods\n📝 **Story:** बीरस के अतीत और उनकी शक्ति के रहस्य।",
    
    "goku": "⭐ **Character: Son Goku**\n🏆 **Role:** Main Protagonist\n💪 **Forms:** SSJ 1-4, Blue, Ultra Instinct\n📝 **Info:** पृथ्वी का रक्षक और ब्रह्मांड का सबसे शक्तिशाली सैयां।",
    
    "beerus": "🟣 **Character: Lord Beerus**\n🏆 **Role:** God of Destruction\n⭐ **Power Level:** Universal+\n📝 **Info:** यूनिवर्स 7 के विनाश के देवता जिन्हें खाना बहुत पसंद है।"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "🐉 **Dragon Ball Expert Bot**\n\n"
        "मैं आपको Rating, Heroes और Release Date सब बताऊंगा।\n"
        "बस ये लिखें: `1986`, `1989`, `2015`, `2024`, `2026`, `Goku`, `Beerus`"
    )
    bot.reply_to(message, text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_info(message):
    user_input = message.text.lower().strip()
    
    if user_input in DB_DATA:
        response = f"{DB_DATA[user_input]}\n\n🔗 {CHANNEL_NAME}"
        bot.reply_to(message, response, parse_mode="Markdown")
    else:
        # किसी और एनीमे के लिए सख्त मनाही
        bot.reply_to(message, "❌ **Data Not Found!**\nमैं सिर्फ Dragon Ball की Rating और जानकारी देता हूँ।")

if __name__ == "__main__":
    bot.polling(none_stop=True)
