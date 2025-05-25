import os
import feedparser
import json
from datetime import datetime
from bs4 import BeautifulSoup
from newspaper import Article
from transformers import pipeline

# Inicializar el modelo de resumen gratuito
summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")

# Leer feeds
with open("feeds.txt", "r") as f:
    feeds = [line.strip() for line in f.readlines() if line.strip()]

# Crear carpeta de noticias
os.makedirs("noticias", exist_ok=True)

def limpiar_titulo(titulo):
    return "".join(c if c.isalnum() or c in " _-" else "_" for c in titulo)[:100]

for feed_url in feeds:
    feed = feedparser.parse(feed_url)
    for entry in feed.entries[:10]:
        try:
            url = entry.link
            titulo = entry.title
            fecha = datetime.now().strftime("%Y-%m-%d")
            nombre_archivo = f"{fecha}_{limpiar_titulo(titulo)}.json"
            ruta_archivo = os.path.join("noticias", nombre_archivo)

            # Saltar si ya existe
            if os.path.exists(ruta_archivo):
                continue

            # Extraer contenido del artículo
            article = Article(url)
            article.download()
            article.parse()
            texto = article.text

            # Si está vacío, ignorar
            if not texto or len(texto.split()) < 50:
                continue

            # Generar resumen
            resumen = summarizer(texto, max_length=200, min_length=50, do_sample=False)[0]["summary_text"]

            # Guardar noticia
            noticia = {
                "titulo": titulo,
                "url": url,
                "resumen": resumen,
                "fecha": fecha
            }
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                json.dump(noticia, f, ensure_ascii=False, indent=2)

            print(f"Noticia guardada: {nombre_archivo}")

        except Exception as e:
            print(f"Error con '{entry.title}': {e}")
