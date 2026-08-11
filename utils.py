import os
import uuid
from datetime import datetime, timedelta

MEDIA_DIR = "media"


def format_price(price, currency="$"):
    price = float(price)
    if price == int(price):
        return f"{int(price)}{currency}"
    return f"{price:.2f}{currency}"


async def save_telegram_photo(bot, file_id, subdir):
    """Telegram file_ids only work with the bot that received them.
    Since we run multiple bots, download the photo once and re-serve it from disk."""
    folder = os.path.join(MEDIA_DIR, subdir)
    os.makedirs(folder, exist_ok=True)
    tg_file = await bot.get_file(file_id)
    path = os.path.join(folder, f"{uuid.uuid4().hex}.jpg")
    await tg_file.download_to_drive(path)
    return path


def generate_khqr_image(account_id, merchant_name, merchant_city, amount, bill_number):
    """Generate a real Cambodia KHQR (EMV-compliant) with the exact amount baked in,
    so the buyer's banking app auto-fills the correct amount when they scan.
    Returns a local PNG path on success, or None on any failure (caller should fall
    back to the static uploaded QR photo instead)."""
    try:
        from bakong_khqr import KHQR
    except ImportError:
        return None

    try:
        khqr = KHQR()
        qr_string = khqr.create_qr(
            account_id=account_id,
            merchant_name=merchant_name,
            merchant_city=merchant_city or "Phnom Penh",
            amount=float(amount),
            currency="USD",
            store_label="Uchiro Store",
            bill_number=bill_number,
            static=False,
        )
        folder = os.path.join(MEDIA_DIR, "khqr")
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"{uuid.uuid4().hex}.png")
        khqr.qr_image(qr_string, output_path=path, format="png")
        return path if os.path.exists(path) else None
    except Exception:
        return None


def warranty_status(approved_at, warranty_days):
    """Human-readable Khmer warranty countdown for an approved order.
    Returns None if the item has no warranty (warranty_days=0) or the order isn't approved yet."""
    if not approved_at or not warranty_days:
        return None
    try:
        approved = datetime.strptime(approved_at, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None
    expires = approved + timedelta(days=warranty_days)
    remaining = (expires - datetime.utcnow()).days
    if remaining < 0:
        return f"❌ Warranty ផុតកំណត់ (ផុតកាលពី {expires.strftime('%d/%m/%Y')})"
    return f"🛡️ Warranty នៅសល់ {remaining} ថ្ងៃ (ផុតកំណត់ {expires.strftime('%d/%m/%Y')})"
