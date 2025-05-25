import os
import requests

BLOGGER_ACCESS_TOKEN = os.getenv("BLOGGER_ACCESS_TOKEN")
BLOG_ID = os.getenv("BLOG_ID")

def publicar_en_blogger(titulo, resumen, link):
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    headers = {
        "Authorization": f"Bearer {BLOGGER_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    contenido = f"<h2>{titulo}</h2><p>{resumen}</p><p><a href='{link}'>Leer más</a></p>"
    data = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": titulo,
        "content": contenido
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"Publicado en Blogger: {titulo}")
    else:
        print(f"Error al publicar en Blogger: {response.status_code}, {response.text}")
