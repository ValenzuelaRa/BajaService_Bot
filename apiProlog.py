import subprocess
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import re
# Importar el módulo subprocess para ejecutar comandos en el sistema operativo
# Importar clases específicas de la librería Telegram para manejar actualizaciones y mensajes
# Importar funciones y clases específicas de la librería Telegram para construir y manejar la aplicación
# Importar el módulo re para trabajar con expresiones regulares

# La función consulta_prolog ejecuta una consulta Prolog en un archivo dado
# y devuelve el resultado como una cadena de texto
# Recibe la consulta a ejecutar y el nombre del archivo Prolog
def consulta_prolog(consulta, archivo):
    try:
        # Construir el comando para ejecutar la consulta Prolog en el archivo especificado
        command = f"swipl -q -g \"{consulta}\" -t halt -f {archivo}"
        # Imprimir el comando a ejecutar
        print(f"Ejecutando comando: {command}")  
        # Ejecutar el comando en el sistema operativo y capturar el resultado
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        # Imprimir el resultado de la consulta
        print(f"Resultado de la consulta: {result.stdout.strip()}")  
        # Verificar si la consulta se ejecutó con éxito
        if result.returncode == 0:
            # Devolver el resultado de la consulta sin espacios adicionales
            return result.stdout.strip()
        else:
            # Imprimir el error si la consulta no se ejecutó correctamente
            print(f"Error al ejecutar la consulta a Prolog: {result.stderr.strip()}")
            return None
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la ejecución de la consulta
        print(f"Error durante la consulta a Prolog: {e}")
        return None

# La función start maneja el comando /start enviado por el usuario
# y muestra un mensaje de bienvenida con botones para elegir una ciudad
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Obtener el usuario que inició la conversación
    user = update.effective_user
    # Crear un teclado con botones para seleccionar una ciudad
    keyboard = [
        [KeyboardButton("Ensenada")],
        [KeyboardButton("Tecate")],
        [KeyboardButton("Tijuana")],
        [KeyboardButton("Rosarito")],
        [KeyboardButton("Mexicali")],
        [KeyboardButton("San Quintín")]
    ]
    # Crear una presentación de teclado con los botones creados
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    # Enviar un mensaje de bienvenida al usuario con el teclado de selección de ciudad
    await update.message.reply_html(
        rf"Hola, {user.mention_html()}! ¿Sobre qué ciudad te gustaría saber?",
        reply_markup=reply_markup,
    )

# La función button maneja los mensajes de texto enviados por el usuario
# y ejecuta una consulta Prolog para obtener información sobre la ciudad seleccionada
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Obtener el mensaje de texto enviado por el usuario
    query = update.message.text
    # Formatear el texto del mensaje para que coincida con el formato de las consultas Prolog
    city_id = formatear_input(query)
    # Construir la consulta Prolog para obtener información sobre la ciudad seleccionada
    prolog_query = f"info_ciudad({city_id}, Descripcion, Logo, Redes), format('~w|~w|~w', [Descripcion, Logo, Redes]), nl."
    # Imprimir la consulta Prolog que se va a ejecutar
    print(f"Consulta Prolog: {prolog_query}")
    # Ejecutar la consulta Prolog y obtener la información sobre la ciudad
    info_completa = consulta_prolog(prolog_query, "ciudades.pl")
    # Verificar si se obtuvo información sobre la ciudad seleccionada
    if info_completa:
        # Separar la información en descripción, logo y redes sociales
        descripcion, logo, redes = info_completa.split('|')
        # Crear un mensaje con la información obtenida
        message = f"Descripción de {query.capitalize()}: {descripcion}\nLogo: {logo}\nRedes Sociales: {redes}"
    else:
        # Si no se encontró información sobre la ciudad, crear un mensaje de error
        message = f"No se encontró información para la ciudad {query.capitalize()}"
    # Enviar el mensaje al usuario con la información obtenida sobre la ciudad
    await update.message.reply_text(text=message)

# La función formatear_input convierte el texto del mensaje a un formato adecuado
# para ser utilizado en consultas Prolog
def formatear_input(texto):
    # Convertir el texto a minúsculas y eliminar espacios y caracteres no alfanuméricos
    texto = re.sub(r'\W+', '', texto.lower().replace(' ', '_'))
    return texto

# La función main es el punto de entrada del programa
def main() -> None:
    # Crear la aplicación de Telegram
    application = Application.builder().token("6324858106:AAHRoqD-4FlVUQyxbXOSqhz4DyXQB4j5MkM").build()
    # Añadir un controlador para el comando /start
    application.add_handler(CommandHandler("start", start))
    # Añadir un controlador para los mensajes de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button))
    # Ejecutar la aplicación para manejar las actualizaciones de Telegram
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# Verificar si el archivo se está ejecutando como script principal
if __name__ == "__main__":
    # Llamar a la función main para iniciar la aplicación
    main()