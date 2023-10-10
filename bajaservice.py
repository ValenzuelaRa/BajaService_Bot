
import logging
from api import encontrar_ciudad_por_id, obtener_ciudad
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,ForceReply
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
    [
        InlineKeyboardButton("Ensenada", callback_data="1"),
        InlineKeyboardButton("Tecate", callback_data="2"),
    ],
    [
        InlineKeyboardButton("Tijuana", callback_data="3"),
        InlineKeyboardButton("Rosarito", callback_data="4"),
    ],
    [
        InlineKeyboardButton("Mexicali", callback_data="5"),
        InlineKeyboardButton("San Quintín", callback_data="6"),
    ],
]


    reply_markup = InlineKeyboardMarkup(keyboard)

    user = update.effective_user
    await update.message.reply_html(
        rf"Hola, {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

    await update.message.reply_text("Baja Service es tu guía confiable para descubrir a los mejores agentes de marketing en Baja California. Nuestro bot te conectará con expertos en contenido, reels, manejo de redes sociales y más. Explora las ciudades de Baja California a continuación para encontrar el marketing que necesitas.", reply_markup=reply_markup)




async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    city_id = int(query.data)  # Convertir el ID de la ciudad de texto a entero

    city_data = encontrar_ciudad_por_id(city_id)
    if city_data is not None:
        # Construye el mensaje de respuesta con formato HTML
        message = f"{city_data['nombre']}\n"
        message += f"Logo: {city_data['logo']}>\n"  
        message += f"Redes Sociales: {city_data['redes']}\n"
        message += f"Descripción: {city_data['descripcion']}\n\n"

        # Envía el mensaje de respuesta al usuario
        await query.answer()
        await query.edit_message_text(text=message, disable_web_page_preview=True)

    else:
        # Maneja el caso en el que la ciudad con el ID dado no se encuentra
        await query.answer(text="Ciudad no encontrada")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hola, {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

    await update.message.reply_text("Baja Service Bot esta disponible para cualquier inconformidad las 24-7 escribenos y uno de nuestros asistentes te respondera de la manera mas inmediata")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6324858106:AAHRoqD-4FlVUQyxbXOSqhz4DyXQB4j5MkM").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

text = (
        "You may choose to add a family member, yourself, show the gathered data, or end the "
        "conversation. To abort, simply type /stop."
    )

    

if __name__ == "__main__":
    main()