import feedparser

def obtener_noticias(feed_url="https://www.elmundo.es/rss/"):
    noticias = []
    feed = feedparser.parse(feed_url)

    for entrada in feed.entries[:5]:  # Puedes cambiar el número de noticias que analiza
        noticia = {
            "titulo": entrada.title,
            "enlace": entrada.link,
            "contenido": entrada.summary if 'summary' in entrada else "",
        }
        noticias.append(noticia)

    return noticias
