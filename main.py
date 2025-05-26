import os

# Crear archivo de credenciales de Blogger desde el secreto
blogger_credentials_json = os.getenv("BLOGGER_CREDENTIALS_JSON")
if blogger_credentials_json:
    credentials_path = "blogger_credentials.json"
    with open(credentials_path, "w") as f:
        f.write(blogger_credentials_json)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
else:
    print("Error: Faltan las credenciales de Blogger.")

# Variables de entorno para Blogger
blogger_blog_id = os.getenv("BLOGGER_BLOG_ID")

# Variables de entorno para Bluesky
bluesky_handle = os.getenv("BLUESKY_HANDLE")
bluesky_app_password = os.getenv("BLUESKY_APP_PASSWORD")

# Variables de entorno para Telegram
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

# Verificaciones
if not blogger_blog_id:
    print("Error: Falta BLOGGER_BLOG_ID.")

if not bluesky_handle or not bluesky_app_password:
    print("Error: Faltan las credenciales de Bluesky.")

if not telegram_bot_token or not telegram_chat_id:
   print("Faltan variables de entorno para Telegram.") 
# Variables de entorno para Blogger
blogger_credentials_json = os.getenv("BLOGGER_CREDENTIALS_JSON")

# Variables de entorno para Bluesky
bluesky_handle = os.getenv("BLUESKY_HANDLE")
bluesky_app_password = os.getenv("BLUESKY_APP_PASSWORD")

# Variables de entorno para Telegram
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
if not blogger_credentials_json:
    print("Error: Faltan las credenciales de Blogger.")

if not bluesky_handle or not bluesky_app_password:
    print("Error: Faltan las credenciales de Bluesky.")

if not telegram_bot_token or not telegram_chat_id:
    print("Faltan variables de entorno para Telegram.")
import os
from modules.noticias import obtener_noticias
from modules.resumen import generar_resumen
from modules.telegram import publicar_en_telegram
from modules.blogger import publicar_en_blogger
from modules.bluesky import publicar_en_bluesky
from newspaper import Article

device = "cpu"
print(f"Device set to use {device}")

noticias = obtener_noticias()
print(f"NOTICIAS: {noticias}")

if not noticias:
    print("NO SE ENCONTRARON NOTICIAS.")
else:
    for noticia in noticias:
        print(f"PROCESANDO NOTICIA: {noticia['titulo']}")
        
        try:
            article = Article(noticia["url"])
            article.download()
            article.parse()
            contenido = article.text

            resumen = generar_resumen(contenido)

            mensaje = f"**{noticia['titulo']}**\n\n{resumen}\n\nFuente: {noticia['url']}"
            
            publicar_en_telegram(mensaje)
            publicar_en_blogger(noticia["titulo"], resumen, noticia["url"])
            publicar_en_bluesky(noticia["titulo"], resumen, noticia["url"])
        
        except Exception as e:
            print(f"ERROR procesando la noticia: {e}")
