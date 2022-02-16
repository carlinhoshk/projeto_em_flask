#!python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Teste Flask'

@app.route('/root')
def root():
    return 'ESSA É A PAGINA ROOT'

@app.route('/segunda')
def welcome():
    return 'Essa é a Segunda Pagina'

app.run()
