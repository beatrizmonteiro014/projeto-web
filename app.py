from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

print (__name__)

@app.route('/')
def inicio():
    return '<h1>Oiiii</h1>'

@app.route('/sobre')
def sobre():
    return '''
<h1 style='color:red'>Meu nome é:</h1>
<p>Beatriz <b>Monteiro<b>
<!-- Tudo que eu pensar em html está aqui -->
'''
@app.route('/curso')
def curso():
    return '''
<p> Desenvolvimento de Software
'''
@app.route('/var')
def variavel():
    palavra = 'Beatriz'
    return f'<h1>Adicionando texto de var: {palavra}</h1>'

@app.route('/idade/<int:ano>')
def idade(ano):
    calculoIdade = 2026 - ano
    return f'Voce tem {calculoIdade} anos!'

@app.route('/salvar/<nome>/produtos')
def salvar(nome):
    return f'Você salvou o produto [ {nome} ] com sucesso!'

@app.route('/html')
def pagiina_html():
    return render_template('index.html')

@app.route('/calcular/<nome>/int:ano')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18:
        status = 'Maior de Idade' # --COLOCAR IGUAL PARA TER 0 18 TAMBÉM ---
    else:
        status = 'Menor de Idade - ACESSO NEGADO'

        return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, nascimento = ano, idade = idade, status = status)
                                                 # - ESQUERDA HTML, DIREITA SITE A ROUTE -










# --- ULTIMA COISA DO ARQUIVO---
if __name__ == '__main__':
    app.run(debug=True)