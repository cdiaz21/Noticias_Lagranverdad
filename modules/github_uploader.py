import base64
import os
from github import Github

def subir_a_github(html, nombre_archivo="index.html"):
    token = os.getenv("MY_GITHUB_TOKEN")
    repo_nombre = os.getenv("MY_GITHUB_REPO")
    ruta_archivo = f"public/{nombre_archivo}"

    g = Github(token)
    repo = g.get_repo(repo_nombre)

    try:
        contenido = repo.get_contents(ruta_archivo)
        repo.update_file(
            path=ruta_archivo,
            message="Actualización automática de noticias",
            content=html,
            sha=contenido.sha
        )
        print("Archivo actualizado en GitHub.")
    except Exception as e:
        repo.create_file(
            path=ruta_archivo,
            message="Creación inicial de archivo de noticias",
            content=html
        )
        print("Archivo creado en GitHub.")
