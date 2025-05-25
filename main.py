from modules.rss import obtener_noticias
from modules.resumen import generar_resumen
from modules.telegram import publicar_en_telegram
from modules.blogger import publicar_en_blogger
from modules.bluesky import publicar_en_bluesky

def main():
    noticias = obtener_noticias()
    for noticia in noticias:
        resumen = generar_resumen(noticia['contenido'])
        publicar_en_telegram(resumen)
        publicar_en_blogger(resumen)
        publicar_en_bluesky(resumen)

if __name__ == "__main__":
    main()
