from datetime import datetime

def generar_html(noticias):
    html = """
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Noticias - La Gran Verdad</title>
    </head>
    <body>
        <h1>Noticias del día - {fecha}</h1>
        <ul>
    """.format(fecha=datetime.now().strftime("%d/%m/%Y"))

    for noticia in noticias:
        html += f"""
        <li>
            <h2>{noticia['titulo']}</h2>
            <p><a href="{noticia['link']}">Leer más</a></p>
            <p>{noticia['resumen']}</p>
        </li>
        """

    html += """
        </ul>
    </body>
    </html>
    """
    return html
