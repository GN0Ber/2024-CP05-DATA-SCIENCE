# app.py

from flask import Flask, render_template, request, redirect, url_for
import os
from scripts.analysis import make_analysis

app = Flask(__name__)

# Configurar a pasta de uploads
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Garantir que a pasta de uploads exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Garantir que a pasta de plots exista
if not os.path.exists('static/plots'):
    os.makedirs('static/plots')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Verificar se o arquivo foi enviado
    if 'file' not in request.files:
        return 'Nenhum arquivo foi enviado.'
    file = request.files['file']
    if file.filename == '':
        return 'Nenhum arquivo selecionado.'
    if file and file.filename.lower().endswith('.csv'):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Executar a análise
        make_analysis(app.config['UPLOAD_FOLDER'], filename)
        # Redirecionar para a página de resultado
        return redirect(url_for('output'))
    else:
        return 'Formato de arquivo não suportado. Por favor, envie um arquivo CSV.'

@app.route('/output')
def output():
    # Renderizar o relatório gerado
    return render_template('output.html')

if __name__ == '__main__':
    app.run(debug=True)
