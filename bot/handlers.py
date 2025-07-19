import os
from telegram import Update
from telegram.ext import ContextTypes
from bot.db import get_counters, reset_counters, set_style, get_style
from bot.styles import afficher_compteurs

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🃏 Bienvenue sur Joker Bot ! Tape /stats pour voir les compteurs.")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    counters = get_counters()
    style = get_style()
    await update.message.reply_text(afficher_compteurs(counters, style))

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reset_counters()
    await update.message.reply_text("🔄 Les compteurs ont été remis à zéro.")

async def change_style(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and context.args[0].isdigit():
        style = int(context.args[0])
        if 1 <= style <= 5:
            set_style(style)
            await update.message.reply_text(f"🎨 Style changé pour le style {style}")
        else:
            await update.message.reply_text("❌ Le style doit être entre 1 et 5.")
    else:
        await update.message.reply_text("❌ Utilisation: /style [1-5]")