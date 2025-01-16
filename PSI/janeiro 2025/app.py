from flask import Flask, render_template,request,redirect,url_for
from database import db
from models import User,Livros


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livraria.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['POST','GET'])
def index():
    usuarios = db.session.execute(db.select(User)).scalars()
    try:
        livros = db.session.execute(db.select(Livros)).scalars()
    except:
        livros = []
    return render_template('listar.html', users = usuarios, livros = livros)

@app.route('/cadastro/user', methods=['POST'])
def cadastro_user():
    if request.method == 'POST':
        nome = request.form['nome']
        user = User(nome=nome)
        db.session.add(user)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/cadastro/livro', methods=['POST'])
def cadastro_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        user = request.form['user']
        user_id = db.session.query(User.id).filter_by(nome = user).first()
        user_id = str(user_id)
        livro = Livros(titulo=titulo, user_id=user_id)
        db.session.add(livro)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/listar')
def listar():
    resultado = db.session.execute(db.select(User)).scalars()
    return render_template('listar.html', resultado = resultado)
