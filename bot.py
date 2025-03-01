import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Chargement des variables d'environnement
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Configuration du logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Commandes de base
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envoie un message quand la commande /start est utilisée."""
    user = update.effective_user
    await update.message.reply_text(f"Bonjour {user.first_name}! Je suis votre bot de consultation documentaire.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envoie un message d'aide quand la commande /help est utilisée."""
    help_text = """
    Commandes disponibles:
    /start - Démarrer le bot
    /help - Afficher l'aide
    """
    await update.message.reply_text(help_text)

# Gestionnaire pour les messages texte
async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Traite les messages texte reçus."""
    await update.message.reply_text(f"Vous avez dit: {update.message.text}")

def main() -> None:
    """Fonction principale pour démarrer le bot."""
    # Vérification de la présence du token
    if not TELEGRAM_TOKEN:
        logger.error("Le token Telegram n'est pas défini dans les variables d'environnement")
        return

    # Création de l'application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Ajout des gestionnaires de commandes
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    
    # Gestionnaire pour les messages texte
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message))

    # Démarrage du bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    logger.info("Bot démarré!")

if __name__ == "__main__":
    main()
