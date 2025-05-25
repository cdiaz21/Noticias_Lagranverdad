from atproto import Client
import os

def publicar_en_bluesky(titulo, contenido, link):
    try:
        client = Client()
        client.login(os.getenv("BLUESKY_USERNAME"), os.getenv("BLUESKY_PASSWORD"))
        mensaje = f"{titulo}\n\n{contenido}\n\n{link}"
        client.send_post(text=mensaje[:300])
    except Exception as e:
        print(f"Error al publicar en Bluesky: {e}")
