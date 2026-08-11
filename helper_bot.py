import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import database as db
from config import (HELPER_BOT_TOKEN, ADMIN_CONTACT_USERNAME, STORE_CHANNEL_USERNAME,
                     STORE_BOT_USERNAME, CREATOR_NAME, CREATOR_TELEGRAM, CREATOR_YOUTUBE)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def promo_kb(extra_rows=None):
    rows = extra_rows or []
    store_url = f"https://t.me/{STORE_BOT_USERNAME}" if STORE_BOT_USERNAME else f"https://t.me/{STORE_CHANNEL_USERNAME}"
    rows.append([InlineKeyboardButton("🛒 ចូលទិញ Account/Fruit/Gamepass", url=store_url)])
    rows.append([InlineKeyboardButton("📞 ទាក់ទង Admin", url=f"https://t.me/{ADMIN_CONTACT_USERNAME}")])
    return InlineKeyboardMarkup(rows)


CREDIT_LINE = f"🙏 Video/Guide ដោយ {CREATOR_NAME} — YouTube: {CREATOR_YOUTUBE}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db.track_user(update.effective_user.id, update.effective_user.username)
    text = (
        "🎮 សួស្តី! Bot នេះជួយអ្នកលេង Blox Fruits ដោយឥតគិតថ្លៃ!\n\n"
        f"{CREDIT_LINE}\n\n"
        "/codes — Code ថ្មីៗ 🎁\n/tierlist — Fruit មួយណាល្អ 🍈\n/guide — វីដេអូបង្រៀន 📺\n\n"
        "ចង់ទិញ Account/Fruit/Gamepass? ចុចប៊ូតុងខាងក្រោម!"
    )
    await update.message.reply_text(text, reply_markup=promo_kb())


async def codes_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    codes = db.get_setting("codes_text")
    text = (f"🎁 Code ថ្មីៗ!\n\n{codes}\n\n👉 ចូល Setting → Redeem Code → Paste → Enter"
            if codes else "😅 មិនទាន់មាន Code ថ្មីទេ! សូមចាំមើលពេលក្រោយ។")
    await update.message.reply_text(text, reply_markup=promo_kb())


async def tierlist_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tierlist = db.get_setting("tierlist_text")
    text = f"🍈 Fruit Tier List:\n\n{tierlist}" if tierlist else "😅 មិនទាន់មាន Tier List ទេ! សូមចាំមើលពេលក្រោយ។"
    await update.message.reply_text(text, reply_markup=promo_kb())


async def guide_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    guides = db.list_guides()
    if not guides:
        return await update.message.reply_text("😅 មិនទាន់មាន Guide ទេ! សូមចាំមើលពេលក្រោយ។", reply_markup=promo_kb())
    kb_rows = [[InlineKeyboardButton(g["title"], callback_data=f"hguide_{g['id']}")] for g in guides]
    await update.message.reply_text(f"📺 ជ្រើសរើស Guide ដែលចង់មើល:\n{CREDIT_LINE}", reply_markup=promo_kb(kb_rows))


async def guide_select_cb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    guide_id = int(query.data.split("_")[1])
    g = db.get_guide(guide_id)
    if not g:
        return await query.message.reply_text("រកមិនឃើញ Guide នេះទេ។")
    await query.message.reply_text(f"📺 {g['title']}\n▶️ {g['video_url']}\n\n{CREDIT_LINE}", reply_markup=promo_kb())


async def on_error(update, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Helper bot error", exc_info=context.error)
    try:
        if isinstance(update, Update) and update.effective_chat:
            await context.bot.send_message(update.effective_chat.id, "⚠️ មានបញ្ហាបច្ចេកទេស សូមព្យាយាមម្តងទៀត។")
    except Exception:
        pass


def build_app():
    app = Application.builder().token(HELPER_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("codes", codes_cmd))
    app.add_handler(CommandHandler("tierlist", tierlist_cmd))
    app.add_handler(CommandHandler("guide", guide_cmd))
    app.add_handler(CallbackQueryHandler(guide_select_cb, pattern=r"^hguide_\d+$"))
    app.add_error_handler(on_error)
    return app


if __name__ == "__main__":
    db.init_db()
    build_app().run_polling()
