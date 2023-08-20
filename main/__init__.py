#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", 15391466, cast=int)
API_HASH = config("API_HASH", 9388b7cc13f3a782b1d5bca493d3aae2)
BOT_TOKEN = config("BOT_TOKEN", 6614754415:AAEarxzaVeNe33FiE524MllPBBSsfpJ-5MQ)
SESSION = config("SESSION", BQBDDq4gLp-YdoeUpAhU3hVzIjoJmNh_j80OZzZfq4YcsKx6x7gpkzfVlOjJ0Rfv1H_J4gWMeFw3niDjNmXTpiRxxJJcDeqiQKroNetOJ-3rkbzMH2X4WGhFu_JHxr79Hlag0ImNge6nELrN5Li3qJWNUdOER1eNdQWiIVNSH-UlOOBVuAjACw78T7jwz0AeF7J9HuI63ZE_HfeadIP7UZFm3vMebEjk_zVBiR1Caf10yd1n6r1r8dEyjoaHmuZdQOYDQgTiP5XQEZZ1wRweeQFz6KyRSMwZaj9OG7yzlOybuSp_EmJXUewzLtrkpsCpeZSfJ8v2tNsJ9fE6Wf86a2weAAAAAWgSk1wA)
FORCESUB = config("FORCESUB", Edu_News_Exams)
AUTH = config("AUTH", 5396638898, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
