"""
Web server for the Uchiro Store Telegram Mini App.
Serves the mini app UI + a read-only JSON API that reads from the same store.db
used by the bots. Also serves product photos from the local media/ folder.

Run standalone for local testing:
    python webapp_server.py
In production this is started by main.py alongside the bots (same process,
different thread) when WEBAPP_PORT is set.
"""
import os
from flask import Flask, jsonify, render_template, send_from_directory

import database as db
from config import STORE_BOT_USERNAME, CATEGORIES, STORE_CHANNEL_USERNAME

app = Flask(__name__, template_folder="webapp/templates")

ASSETS_DIR = os.path.join(os.getcwd(), "webapp", "assets")


@app.route("/")
def index():
    logo_path = os.path.join(ASSETS_DIR, "logo.png")
    music_path = os.path.join(ASSETS_DIR, "music.mp3")
    return render_template(
        "index.html",
        bot_username=STORE_BOT_USERNAME,
        channel_username=STORE_CHANNEL_USERNAME,
        logo_url="/assets/logo.png" if os.path.exists(logo_path) else None,
        music_url="/assets/music.mp3" if os.path.exists(music_path) else None,
    )


@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory(ASSETS_DIR, filename)


@app.route("/api/items")
def api_items():
    all_items = db.get_all_items()
    items = []
    for it in all_items:
        if not (it["active"] and it["quantity"] > 0):
            continue
        # photo_file_id is stored as a relative path like "media/items/xxxx.jpg"
        photo_url = f"/{it['photo_file_id']}" if it["photo_file_id"] else None
        items.append({
            "id": it["id"],
            "category": it["category"],
            "name": it["name"],
            "price": it["price"],
            "description": it["description"],
            "quantity": it["quantity"],
            "photo_url": photo_url,
        })
    return jsonify({"items": items, "categories": CATEGORIES})


@app.route("/media/<path:filename>")
def media(filename):
    return send_from_directory(os.path.join(os.getcwd(), "media"), filename)


@app.route("/health")
def health():
    return "ok"


def run(port=None):
    port = port or int(os.getenv("WEBAPP_PORT", "8080"))
    db.init_db()
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    run()
