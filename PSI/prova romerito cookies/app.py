from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

dictmensagens = {}

#Requisitos da prova (ToDo List):
#1: Logar um usuário com nome
#2: Levar o usuário logado para uma página com um formulário de mensagens
#3: Poder levar o ususuário para uma página que mostra as mensagens enviadas por ele

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        template = render_template('login.html')
        response = make_response(template)
        response.set_cookie('user', nome)
        return response
    
    return render_template('login.html')

@app.route('/mensagens', methods=['POST', 'GET'])
def mensagens():
    usuario = request.cookies.get('user')

    if str(usuario) not in dictmensagens: #Ve se ja existe uma chave com o nome o usuario
        dictmensagens[str(usuario)] = [] #Caso não exista, cria uma lista vazia pra guardar as mensagens dele
    
    if request.method == 'POST':
        mensagem = request.form['mensagem'] #Pega a mensagem do formulario
        lista = dictmensagens[str(usuario)] #Pega a lista de mensagens do usuario ''logado''
        lista.append(mensagem) #Adciona na lista a mensagem inserida
        dictmensagens[str(usuario)] = lista #Atualiza a lista do dicionario com a nova lista
        
        return redirect(url_for('mensagens')) #recarrega a página
    
    return render_template('mensagens.html', mensagens = dictmensagens[usuario]) #Envia a lista de mensagens associada ao nome do user
    