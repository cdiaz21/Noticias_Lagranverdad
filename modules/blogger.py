from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

# Asegúrate de que estas variables de entorno estén configuradas correctamente
BLOGGER_BLOG_ID = os.getenv("BLOGGER_BLOG_ID")
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

def publicar_en_blogger(titulo, resumen, url):
    if not BLOGGER_BLOG_ID or not SERVICE_ACCOUNT_FILE:
        print("Error: Faltan las credenciales de Blogger.")
        return

    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=["https://www.googleapis.com/auth/blogger"]
        )
        service = build("blogger", "v3", credentials=credentials)
        post = {
            "title": titulo,
            "content": f"{resumen}<br><br><a href='{url}'>Leer más</a>"
        }
        service.posts().insert(blogId=BLOGGER_BLOG_ID, body=post).execute()
        print("Entrada publicada en Blogger correctamente.")
    except Exception as e:
        print(f"Error al publicar en Blogger: {e}")
