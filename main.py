import feedparser
from newspaper import Article
from transformers import pipeline
from datetime import datetime
import os

# CONFIG
RSS_FEED_URLS = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
]

# Crear carpeta de salida
os.makedirs("noticias", exist_ok=True)

# Cargar modelo de resumen
summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")

# Procesar feeds
for url in RSS_FEED_URLS:
    feed = feedparser.parse(url)

    for entry in feed.entries[:2]:  # solo 2 por feed para ejemplo
        try:
            article = Article(entry.link)
            article.download()
            article.parse()

            texto = article.text[:1000]  # Limitar longitud para evitar errores
            resumen = summarizer(texto)[0]['summary_text']

            titulo_archivo = entry.title.strip().replace(" ", "_")[:50]
            fecha = datetime.utcnow().strftime("%Y-%m-%d")
            nombre = f"noticias/{fecha}_{titulo_archivo}.md"

            with open(nombre, "w", encoding="utf-8") as f:
                f.write(f"# {entry.title}\n\n")
                f.write(f"**Link original:** {entry.link}\n\n")
                f.write(f"**Resumen generado por IA:**\n\n")
                f.write(resumen)

            print(f"Generado: {nombre}")

        except Exception as e:
            print(f"Error con {entry.link}: {e}")
