import logging
import os
from telegram import Update, ChatMemberUpdated
from telegram.ext import (
    ApplicationBuilder, ContextTypes, CommandHandler,
    MessageHandler, ChatMemberHandler, filters
)
from bot.handlers import start, stats, reset, change_style
from bot.utils import traiter_message, traiter_message_edite
from bot.db import setup_db

# Configuration du logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Configuration PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

async def handle_new_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.my_chat_member and update.my_chat_member.new_chat_member.status == "member":
        await context.bot.send_message(
            chat_id=update.my_chat_member.chat.id,
            text="""🃏 Salut tout le monde ! 🃏

Je suis le Bot Joker, votre assistant de comptage pour les jeux de cartes ! Je suis là pour compter automatiquement le nombre de fois que les symboles ❤️ ♦️ ♣️ ♠️ apparaissent dans vos messages.

🎯 Mon rôle :
• Je surveille les messages avec #n[numéro]
• Je compte les symboles dans les parenthèses des messages validés (✅ 🔰)
• Je tiens le score à jour automatiquement

📋 Commandes disponibles :
• /start - Message de bienvenue
• /stats - Voir les statistiques actuelles
• /style 1-5 - Changer l'affichage
• /reset - Remettre les compteurs à zéro

Que les jeux commencent ! 🎮✨"""
        )

def main():
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    setup_db()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(CommandHandler("style", change_style))
    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, traiter_message))
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_CHANNEL_POST, traiter_message_edite))
    app.add_handler(ChatMemberHandler(handle_new_chat_member, ChatMemberHandler.MY_CHAT_MEMBER))

    port = int(os.getenv("PORT", "8080"))
    app.run_polling()

if __name__ == "__main__":
    main()