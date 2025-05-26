import os
import base64
from modules.noticias import obtener_noticias
from modules.resumen import generar_resumen
from modules.telegram import publicar_en_telegram
from modules.blogger import publicar_en_blogger
from modules.bluesky import publicar_en_bluesky
from newspaper import Article

# Configurar dispositivo
device = "cpu"
print(f"Device set to use {device}")

# Decodificar credenciales Blogger
base64_creds = os.getenv("BLOGGER_CREDENTIALS_JSON_BASE64")
if base64_creds:
    with open("service_account.json", "wb") as f:
        f.write(base64.b64decode(base64_creds))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"
else:
    print("Error: Faltan las credenciales de Blogger.")

# Verificar credenciales necesarias
if not os.getenv("BLOGGER_BLOG_ID"):
    print("Error: Falta el ID del blog de Blogger.")
if not os.getenv("BLUESKY_HANDLE") or not os.getenv("BLUESKY_APP_PASSWORD"):
    print("Error: Faltan las credenciales de Bluesky.")
if not os.getenv("TELEGRAM_BOT_TOKEN") or not os.getenv("TELEGRAM_CHAT_ID"):
    print("Faltan variables de entorno para Telegram.")

# Obtener noticias
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
