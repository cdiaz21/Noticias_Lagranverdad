from transformers import pipeline

# Cargamos el pipeline de resumen
resumidor = pipeline("summarization", model="facebook/bart-large-cnn")

def generar_resumen(texto, max_length=130, min_length=30):
    if not texto:
        return "Sin contenido para resumir."

    try:
        resumen = resumidor(texto, max_length=max_length, min_length=min_length, do_sample=False)
        return resumen[0]['summary_text']
    except Exception as e:
        print("Error generando resumen:", e)
        return "Resumen no disponible."
