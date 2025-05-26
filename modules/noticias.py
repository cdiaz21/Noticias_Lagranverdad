import feedparser

FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

def obtener_noticias(max_noticias=5):
    noticias = []
    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:max_noticias]:
            noticias.append({
                "titulo": entry.title,
                "url": entry.link
            })
    return noticias
