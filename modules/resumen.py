from newspaper import Article
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generar_resumen(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        texto = article.text

        if not texto.strip():
            raise ValueError("Artículo vacío")

        resumen = summarizer(texto, max_length=130, min_length=30, do_sample=False)
        return resumen[0]['summary_text']
    except Exception as e:
        raise RuntimeError(f"Error generando resumen: {str(e)}")
