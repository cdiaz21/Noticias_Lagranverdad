from bs4 import BeautifulSoup
import openai  # Cambié 'from openai import OpenAI' a 'import openai'
import os
import requests

# Configuración de la clave API
openai.api_key = os.getenv("OPENAI_API_KEY")  # Asegúrate de que tienes tu clave API configurada en las variables de entorno

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
    response = openai.ChatCompletion.create(  # Cambié 'client.chat.completions.create' a 'openai.ChatCompletion.create'
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()  # Cambié 'message.content' a 'message['content']'

# Ejemplo de uso
if __name__ == "__main__":
    noticias = get_news()
    for noticia in noticias:
        print(noticia)
