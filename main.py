import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import os
import datetime
import json

# Inicializar el modelo de Hugging Face
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Lista de URLs a analizar
urls = [
    "https://elpais.com/internacional/2025-05-25/netanyahu-impulsa-en-gaza-la-agenda-mas-radical-de-la-extrema-derecha-israeli.html",
    "https://elpais.com/espana/2025-05-25/albares-pide-embargo-armas-israel.html"
]

# Carpeta de salida
OUTPUT_DIR = "noticias"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extraer_contenido(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        titulo = soup.find("title").get_text()
        parrafos = soup.find_all("p")
        texto = " ".join(p.get_text() for p in parrafos)
        return titulo.strip(), texto.strip()
    except Exception as e:
        print(f"Error extrayendo texto de {url}: {e}")
        return None, None

def generar_resumen(texto):
    try:
        if len(texto) > 1024:
            texto = texto[:1024]
        resumen = summarizer(texto, max_length=150, min_length=40, do_sample=False)
        return resumen[0]['summary_text']
    except Exception as e:
        print(f"Error generando resumen: {e}")
        return None

def guardar_noticia(titulo, resumen):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"{fecha}_{titulo[:50].replace(' ', '_').replace('/', '')}.json"
    ruta = os.path.join(OUTPUT_DIR, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump({"titulo": titulo, "resumen": resumen, "fecha": fecha}, f, ensure_ascii=False, indent=2)
    print(f"Guardado: {ruta}")

def main():
    print("Iniciando generación de noticias...")
    for url in urls:
        titulo, texto = extraer_contenido(url)
        if titulo and texto:
            resumen = generar_resumen(texto)
            if resumen:
                guardar_noticia(titulo, resumen)
            else:
                print(f"No se pudo generar resumen para: {titulo}")
        else:
            print(f"No se pudo procesar: {url}")

if __name__ == "__main__":
    main()
