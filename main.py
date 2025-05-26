import os
from modules.noticias import obtener_noticias
from modules.resumen import generar_resumen
from modules.telegram import publicar_en_telegram
from modules.blogger import publicar_en_blogger
from modules.bluesky import publicar_en_bluesky
from newspaper import Article

device = "cpu"
print(f"Device set to use {device}")

noticias = obtener_noticias()
print(f"NOTICIAS: {noticias}")

if not noticias:
    print("NO SE ENCONTRARON NOTICIAS.")
else:
    for noticia in noticias:
        print(f"PROCESANDO NOTICIA: {noticia['titulo']}")
        
        try:
            article = Article(noticia["url"])
            article.download()
            article.parse()
            contenido = article.text

            resumen = generar_resumen(contenido)

            mensaje = f"<b>{noticia['titulo']}</b>\n\n{resumen}\n\nFuente: {noticia['url']}"

            publicar_en_telegram(mensaje)
            publicar_en_blogger(noticia["titulo"], resumen, noticia["url"])
            publicar_en_bluesky(noticia["titulo"], resumen, noticia["url"])
        
        except Exception as e:
            print(f"ERROR procesando la noticia: {e}")
