import feedparser

# Puedes agregar más feeds aquí
FEEDS = [
    "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/internacional.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://www.theguardian.com/world/rss"
]

def obtener_noticias():
    noticias = []

    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
        for entrada in feed.entries:
            if "title" in entrada and "summary" in entrada and "link" in entrada:
                titulo = entrada.title
                resumen = entrada.summary
                url = entrada.link

                # Filtro básico opcional (por ejemplo, evitar duplicados o por palabra clave)
                if len(resumen) > 100 and "deportes" not in titulo.lower():
                    noticias.append({
                        "titulo": titulo,
                        "resumen": resumen,
                        "url": url
                    })

            if len(noticias) >= 3:  # Solo tomamos 3 noticias para limitar la carga
                break

    return noticias
