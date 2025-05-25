from modules.rss import obtener_noticias
from modules.resumen import generar_resumen
from modules.telegram import enviar_telegram
from modules.blogger import publicar_en_blogger
from modules.bluesky import publicar_en_bluesky

noticias = obtener_noticias()
print("NOTICIAS:", noticias)  # DEBUG: muestra las noticias obtenidas

if not noticias:
    print("NO SE ENCONTRARON NOTICIAS.")
else:
    for noticia in noticias:
        print(f"PROCESANDO NOTICIA: {noticia['titulo']}")  # DEBUG
        resumen = generar_resumen(noticia["contenido"])
        print(f"RESUMEN: {resumen}")  # DEBUG

        # Aquí puedes decidir cuál de estas publicar o activar todas:
        enviar_telegram(noticia["titulo"], resumen, noticia["url"])
        publicar_en_blogger(noticia["titulo"], resumen, noticia["url"])
        publicar_en_bluesky(noticia["titulo"], resumen, noticia["url"])

print("¡Proceso de noticias completado correctamente!")
