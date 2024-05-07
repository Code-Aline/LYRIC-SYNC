import PyPDF2
from deep_translator import GoogleTranslator

def traduzir(caminho_arquivo_pdf):
    pdf = open (caminho_arquivo_pdf, 'rb')
    reader = PyPDF2.PdfReader(pdf)
    pagina = reader.pages[0]

    extracao = pagina.extract_text()

    tradutor = GoogleTranslator(source='en', target='pt')

    texto = pagina.extract_text()

    traducao = tradutor.translate(texto)

    return traducao

