from atproto import Client
import os

# Asegúrate de que estas variables de entorno estén configuradas correctamente
BLUESKY_HANDLE = os.getenv("BLUESKY_HANDLE")
BLUESKY_PASSWORD = os.getenv("BLUESKY_PASSWORD")

def publicar_en_bluesky(titulo, resumen, url):
    if not BLUESKY_HANDLE or not BLUESKY_PASSWORD:
        print("Error: Faltan las credenciales de Bluesky.")
        return

    try:
        client = Client()
        client.login(BLUESKY_HANDLE, BLUESKY_PASSWORD)
        texto = f"📰 {titulo}\n\n{resumen}\n\n🔗 {url}"
        client.send_post(text=texto)
        print("Publicación realizada en Bluesky correctamente.")
    except Exception as e:
        print(f"Error al publicar en Bluesky: {e}")
