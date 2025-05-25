import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import time

# Inicializa el pipeline de Hugging Face para resumen
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Lista de URLs de noticias
urls = [
    "https://elpais.com/internacional/2024-05-24/netanyahu-impulsa-en-gaza-la-agenda-mas-radical-de-la-extrema-derecha-israeli.html",
    "https://elpais.com/internacional/2024-05-24/ultima-hora-del-conflicto-en-oriente-proximo-en-directo.html",
    "https://elpais.com/deportes/2024-05-24/rafa-nadal-se-despide-de-roland-garros.html",
    # Añade más URLs si quieres
]

def obtener_texto_noticia(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        texto = " ".join([p.get_text() for p in soup.find_all('p')])
        return texto.strip()
    except Exception as e:
        print(f"Error al obtener el contenido de {url}: {e}")
        return ""

def resumir_noticia(texto):
    try:
        resumen = summarizer(texto, max_length=180, min_length=50, do_sample=False)
        return resumen[0]['summary_text']
    except Exception as e:
        print(f"Error generando resumen: {e}")
        return "Resumen no disponible."

def main():
    print("Iniciando generación de noticias...")
    noticias_resumidas = []

    for url in urls:
        texto = obtener_texto_noticia(url)
        if texto:
            print(f"Generando resumen para: {url}")
            resumen = resumir_noticia(texto)
            noticias_resumidas.append({
                "url": url,
                "resumen": resumen
            })
            time.sleep(2)  # Evita sobrecargar el servidor

    print("\nNoticias generadas:")
    for noticia in noticias_resumidas:
        print(f"\n{noticia['url']}\nResumen: {noticia['resumen']}")

if __name__ == "__main__":
    main()
