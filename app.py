from flask import Flask, render_template, request, make_response, url_for, redirect, session

app = Flask(__name__)

bancodados = {}

app.config['SECRET_KEY'] = 'superdificil'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():

    if request.method == "GET":
        return render_template('login.html')
    else: 
        #Pegando informações do formulario nas paginas html
        nome = request.form['nome']
        senha = request.form['senha']

        #Checa se o nome existe no banco e a senha está certa
        if nome in bancodados and bancodados[nome] == senha:
            #define o usuario e redireciona para o dashboard
            session['user'] = nome
            return redirect(url_for('dash'))
        else:
            return 'Senha incorreta ou cadastro não encontrado'


@app.route('/dashboard')
def dash():

    #Checa se tem um usuario ativo na sessão, se não tiver, te joga de volta pra pagina inicial
    if 'user' not in session:
        return redirect(url_for('index'))

    #Se passar reto do if not, significa que tem um usuario ativo em sessão, então redireciona para a pagina do dashboard 
    return render_template('dashboard.html', nome = session['user'])

@app.route('/register', methods=['GET','POST'])
def register():
    # Romerito fez isso daq mas ta dando errado, esquece
    # if 'user' in session:
    #     return redirect(url_for('dash'))

    if request.method == 'GET':
        return render_template('register.html')
    else:
        #Pegando as informações do formulario nas paginas html
        nome = request.form['nome']
        senha = request.form['senha']
        
        #Vendo se ja não existe esse usuario no "banco de dados"
        if nome not in bancodados:
            #Se não tiver, joga no banco
            bancodados[nome] = senha
        else:
            #Se ja existir, redireciona pra pagina de login
            return redirect(url_for('login'))
        
        #Define o nome do usuario da sessão com o nome colocado no formulario e redireciona pro dashboard
        session['user'] = nome
        return redirect(url_for('dash'))

@app.route('/logout', methods=['POST'])
def logout():
    #Vê se tem um usuario ativo para remover da session e redirecionar para o index
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))