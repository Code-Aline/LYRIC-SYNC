import speech_recognition as sr
from yt_dlp import YoutubeDL
import whisper

def transcrever(url, filename='audio'):
    # Opções para o download do áudio do YouTube
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': filename,
    }

    # Baixar o áudio do vídeo do YouTube
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Carrega o modelo de transcrição de áudio
    modelo = whisper.load_model('small')

    # Transcreve o áudio
    resposta = modelo.transcribe(filename + '.mp3')

    # Retorna o texto da transcrição
    return resposta['text']

