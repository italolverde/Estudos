from flask import Flask, make_response, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    cookies = request.cookies
    return render_template('index.html',cookies = cookies)

@app.route('/inserir', methods = ['POST', 'GET'])
def inserir():
    if request.method == 'POST':
        nome = request.form['nome_cookie']
        template = redirect(url_for('index'))
        response  = make_response(template)
        response.set_cookie(nome , nome)
        return response

@app.route('/remover', methods = ['POST', 'GET'])
def remover():
    if request.method == 'POST':
        nome_cookie = request.form['nome_cookie']
        template = redirect(url_for('index'))
        response = make_response(template)
        response.delete_cookie(nome_cookie)
        return response
