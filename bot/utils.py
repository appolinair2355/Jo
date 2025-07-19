import re
from telegram import Update
from telegram.ext import ContextTypes
from bot.db import get_processed_ids, save_processed_id, update_counters
from bot.styles import count_symbols

def extract_cards_parenthese(text: str):
    match = re.search(r'[(](.*?)[)]', text)
    if not match:
        return []
    contenu = match.group(1)
    return re.findall(r'[❤️♦️♣️♠️]', contenu)

async def traiter_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post
    if not message or not message.text:
        return
    text = message.text

    # Attendre que le message soit complet
    if any(symbole in text for symbole in ['⏰', '▶', '🕐', '➡️']):
        return

    if '✅' not in text and '🔰' not in text:
        return

    if '#n' not in text:
        return

    message_id = message.message_id
    if message_id in get_processed_ids():
        return

    cartes = extract_cards_parenthese(text)
    if len(cartes) == 3:
        update_counters(cartes)
        save_processed_id(message_id)

async def traiter_message_edite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.edited_channel_post
    if not message or not message.text:
        return
    await traiter_message(update, context)