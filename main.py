import json
from modules.resumen import generar_resumen
from resumen import generar_resumen
from bluesky import publicar_bluesky
from telegram import publicar_telegram
from blogger import publicar_blogger

# Ejemplo de fuente de noticias (puedes sustituir esto por tu scraper real)
def cargar_noticias():
    return [
        {
            "titulo": "Ejemplo de noticia",
            "url": "https://www.bbc.com/news/world-europe-68125849"
        },
        {
            "titulo": "Noticia inválida",
            "url": "https://www.ejemplo.com/falla"
        }
    ]

# Procesar y publicar noticias
def procesar_noticias():
    noticias = cargar_noticias()

    for noticia in noticias:
        titulo = noticia["titulo"]
        url = noticia["url"]

        print(f"\n📥 Procesando: {titulo}")
        try:
            resumen = generar_resumen(url)
        except Exception as e:
            print(f"❌ Error al generar resumen: {e}")
            continue

        contenido = f"📰 {titulo}\n\n🧠 {resumen}\n\n🔗 {url}"

        # Publicar en Bluesky
        try:
            publicar_bluesky(contenido)
            print("✅ Publicado en Bluesky")
        except Exception as e:
            print(f"⚠️ Error en Bluesky: {e}")

        # Publicar en Telegram
        try:
            publicar_telegram(contenido)
            print("✅ Publicado en Telegram")
        except Exception as e:
            print(f"⚠️ Error en Telegram: {e}")

        # Publicar en Blogger
        try:
            publicar_blogger(titulo, resumen, url)
            print("✅ Publicado en Blogger")
        except Exception as e:
            print(f"⚠️ Error en Blogger: {e}")

# Ejecutar todo
if __name__ == "__main__":
    procesar_noticias()
