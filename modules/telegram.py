from telegram import Bot
import os

# Asegúrate de que estas variables de entorno estén configuradas correctamente
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_telegram(titulo, resumen, url):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Error: Faltan las credenciales de Telegram.")
        return

    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    mensaje = f"📰 {titulo}\n\n{resumen}\n\n🔗 {url}"
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=mensaje)
        print("Mensaje enviado a Telegram correctamente.")
    except Exception as e:
        print(f"Error al enviar mensaje a Telegram: {e}")
