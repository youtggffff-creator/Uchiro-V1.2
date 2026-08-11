import os

ADMIN_BOT_TOKEN = os.getenv("ADMIN_BOT_TOKEN", "8906347735:AAHiHksd28uRWd5YdsVTynYMv9vCz5rPuxg")
STORE_BOT_TOKEN = os.getenv("STORE_BOT_TOKEN", "8546642077:AAGeBkvSJ9NS8D3C8bEg_xdIjwMXftYJ0bU")
HELPER_BOT_TOKEN = os.getenv("HELPER_BOT_TOKEN", "PUT_YOUR_HELPER_BOT_TOKEN_HERE")

# Owner(s) - can add/remove other sellers. Comma separated telegram user ids.
OWNER_IDS = [int(x) for x in os.getenv("OWNER_IDS", "6594079594").split(",") if x.strip().isdigit()]

STORE_NAME = "Uchiro Store 🇰🇭"
CURRENCY = "$"
CATEGORIES = ["Account", "Fruit", "Gamepass", "Evade", "Robux", "Blade Ball", "MM2"]
DB_PATH = os.getenv("DB_PATH", "store.db")

ADMIN_CONTACT_USERNAME = "noreakyout"  # @noreakyout
STORE_CHANNEL_USERNAME = "uchirostore"  # t.me/uchirostore
STORE_BOT_USERNAME = os.getenv("STORE_BOT_USERNAME", "UchiroStore_BOT")  # e.g. "UchiroStoreBot" (no @), for direct bot deep-link
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://uchiro-v1-production.up.railway.app/")  # public https URL of the Mini App (webapp_server.py), e.g. https://yourapp.up.railway.app

CREATOR_NAME = "Rock Xebec1803"
CREATOR_TELEGRAM = "rockxebec1803"
CREATOR_YOUTUBE = "https://www.youtube.com/@xebec1803"
