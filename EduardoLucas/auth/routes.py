from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from core.models import User
from database import session
from sqlalchemy import update #mds, esses import não usado

auth_bp = Blueprint('auth', 'auth', template_folder='templates')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('core.users'))

    if request.method == 'POST':

        nome = request.form['nome']
        senha = request.form['senha']
        #Select * From users Where user_nome = nome_formulario, user_senha = senha_formulario Limit 1
        usuario = session.query(User).where(User.nome == nome, User.senha == senha).first()
        if usuario:
            login_user(usuario)
            return redirect(url_for('core.users'))
        else:
            flash('*Senha ou Usuário incorreto')
        
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        user = User(nome=nome, email=email, senha=senha)
        equal = session.query(User).where(
            User.nome == nome, 
            User.email == email).count()
        
        if not equal:
            session.add(user)
            session.commit()
            login_user(user)
            return redirect(url_for('core.users'))
        else:
            flash('*Usuário já cadastrado')

    return render_template('register.html')


@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))

@auth_bp.route('/cadastro_gerencia',methods=['POST','GET'])
@login_required
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        user = User(nome=nome, email=email, senha=senha, gerente_id= User.get_id(current_user))
        #Exemplo de select com where: 
        equal = session.query(User).where(
            User.nome == nome, 
            User.email == email).count()
        
        if not equal:
            session.add(user)
            session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('*Usuário já cadastrado')
    return render_template('cadastro.html')

@auth_bp.route('/editar', methods=['POST','GET'])
def editar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        #Esse comentário abaixo é dele :P
        # NÃO SEI COMO ATUALIZA COM SQLALCHEMY MAS PELO MENOS O FORM TÁ CRIADO
        #Mas ele tava querendo dar um update, pesquisando aqui encontrei 2 jeito de fazer
        #!!!!Aparentemente!!!! você pode pegar um usuário e depois mudar o valor dele normalmente como objeto
        #Exemplo: user.nome = 'novo_nome' e depois session.commit()
        #E outro jeito é usar o método update(), mas o código fica gigantesco, ficaria melhor você mesma pesquisar
        #chatgpt explicou bonitinho aqui, recomendo
        return redirect(url_for('core.users'))
    return render_template('editar.html')