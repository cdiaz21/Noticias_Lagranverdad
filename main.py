from modules.news_fetcher import get_news
from modules.html_generator import generar_html
from modules.github_uploader import subir_a_github

def main():
    print("Iniciando generación de noticias...")

    noticias = get_news()

    if not noticias:
        print("No se generaron noticias.")
        return

    print("Generando HTML...")
    html = generar_html(noticias)

    print("Subiendo a GitHub...")
    subir_a_github(html)

    print("Proceso completado exitosamente.")

if __name__ == "__main__":
    main()
