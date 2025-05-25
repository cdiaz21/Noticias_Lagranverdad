import feedparser
from openai import OpenAI
import os

# Inicializa el cliente con la clave desde variables de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Función para generar un resumen con OpenAI
def generar_resumen(titulo, link):
    prompt = f"Genera un resumen breve y objetivo de esta noticia:\n\nTítulo: {titulo}\nLink: {link}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# Función para obtener noticias de varias fuentes RSS y resumirlas
def get_news():
    urls = [
        "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada",
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://feeds.bbci.co.uk/news/rss.xml"
    ]

    noticias = []

    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # Solo toma las primeras 3 noticias por fuente
            titulo = entry.title
            link = entry.link

            try:
                resumen = generar_resumen(titulo, link)
                noticias.append({
                    "titulo": titulo,
                    "link": link,
                    "resumen": resumen
                })
            except Exception as e:
                print(f"Error generando resumen para '{titulo}': {str(e)}")

    return noticias
