import os
from modules.news_fetcher import get_news
from modules.blogger import publicar_en_blogger
from modules.telegram import publicar_en_telegram
from modules.bluesky import publicar_en_bluesky
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Iniciando generación de noticias...")
    noticias = get_news()
    for noticia in noticias:
        resumen = noticia["resumen"]
        titulo = noticia["titulo"]
        link = noticia["link"]

        publicar_en_blogger(titulo, resumen, link)
        publicar_en_telegram(titulo, resumen, link)
        publicar_en_bluesky(titulo, resumen, link)

if __name__ == "__main__":
    main()
