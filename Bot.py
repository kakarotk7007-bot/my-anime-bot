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
    "movies": "
    
