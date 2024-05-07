from googletrans import Translator
from nltk.sentiment import SentimentIntensityAnalyzer

def traduzir_para_ingles(mensagem):
    translator = Translator()
    traducao = translator.translate(mensagem, src='pt', dest='en')
    return traducao.text

def analisar_sentimento(texto):
    sia = SentimentIntensityAnalyzer()
    polaridade = sia.polarity_scores(texto)['compound']
    if polaridade > 0:
        return '''Agradecemos seu feedback! \n
                ficamos feliz que sua experiencia tenha sido Positiva.'''
    elif polaridade < 0:
        return '''Agradecemos seu feedback! \n
                ficamos triste que sua experiencia tenha sido negativa. Estamos trabalhando para realizar melhorias.'''
    else:
        return '''Agradecemos seu feedback!'''

