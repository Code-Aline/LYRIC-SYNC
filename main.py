from flask import Flask, render_template, request,redirect, flash, session, jsonify, send_from_directory
from pathlib import Path
from transcricao import transcrever
from tradutorpdf import traduzir
from sentimentos import analisar_sentimento,traduzir_para_ingles
import os

caminho = Path(__file__)
pasta_atual = caminho.parent

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index")
def inicioPage():
    return render_template('index.html')

@app.route('/contato')
def contatoPage():
    return render_template('contato.html')

@app.route('/servicos')
def servicosPage():
    return render_template('servicos.html')

@app.route('/sobre')
def sobrePage():
    return render_template('sobre.html')

@app.route("/upload", methods=['POST'])
def upload(): 
    arquivo = request.files.get('documento')
    nome_arquivo = str('teste') + '.pdf'
    caminho_arquivo = arquivo.save(os.path.join(f'{pasta_atual}/arquivos/', nome_arquivo))

    flash('Arquivo salvo')
    caminho_arquivo_pdf = 'arquivos/teste.pdf'
    traducao = traduzir(caminho_arquivo_pdf)
    
    return render_template('servicos.html', textoTraduzido=traducao)


@app.route("/transcricao", methods=['POST'])
def transcrever_audio():
    url = request.form['url']
    texto_transcrito = transcrever(url)

    return render_template('servicos.html', texto=texto_transcrito)

@app.route('/enviar', methods=['POST'])
def enviar_mensagem():
    mensagem = request.form['mensagem']
    tradutor = traduzir_para_ingles(mensagem)
    sentimento = analisar_sentimento(tradutor)
    return render_template('contato.html', mensagemSite=sentimento)

if __name__ in "__main__":
    app.run(debug=True)  