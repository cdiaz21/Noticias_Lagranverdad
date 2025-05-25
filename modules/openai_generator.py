import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generar_titulares(titulo, contenido):
    prompt = f"Genera un titular llamativo y un resumen para la siguiente noticia:\nTítulo original: {titulo}\nContenido: {contenido}"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    generado = respuesta["choices"][0]["message"]["content"]
    partes = generado.split("\n", 1)
    titulo_generado = partes[0]
    contenido_generado = partes[1] if len(partes) > 1 else contenido
    return titulo_generado.strip(), contenido_generado.strip()
