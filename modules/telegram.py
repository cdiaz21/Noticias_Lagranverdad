import os
import requests

def publicar_en_telegram(mensaje):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Faltan variables de entorno para Telegram.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensaje,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Error al enviar mensaje: {response.text}")
        else:
            print("Mensaje enviado a Telegram correctamente.")
    except Exception as e:
        print(f"Error al conectar con la API de Telegram: {e}")
