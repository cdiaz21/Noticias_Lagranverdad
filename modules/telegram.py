import requests
import os

def publicar_en_telegram(titulo, contenido, link):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    mensaje = f"**{titulo}**\n\n{contenido}\n\n[Leer más]({link})"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    r = requests.post(url, data=data)
    if r.status_code != 200:
        print(f"Error al enviar a Telegram: {r.text}")
