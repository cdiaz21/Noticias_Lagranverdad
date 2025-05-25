from bs4 import BeautifulSoup
from openai import OpenAI
import os
import requests

client = OpenAI()  # Nuevo cliente OpenAI

def get_news():
    feed_urls = [
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://rss.cnn.com/rss/edition.rss"
    ]
    noticias = []
    for url in feed_urls:
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "lxml-xml")
        items = soup.findAll("item")
        for item in items[:3]:
            titulo = item.title.text
            link = item.link.text
            resumen = generar_resumen(titulo, link)
            noticias.append({"titulo": titulo, "link": link, "resumen": resumen})
    return noticias

def generar_resumen(titulo, link):
    prompt = f"Resume la siguiente noticia en 3 frases breves y claras: {titulo}\n{link}"
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return respuesta.choices[0].message.content.strip()
