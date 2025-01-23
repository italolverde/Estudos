from flask import Blueprint, render_template
from flask_login import login_required
from database import session
from core.models import User

core = Blueprint('core', 'core', template_folder='templates')

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/users')
@login_required
def users():

    #Esse session.query(classe) significa um select na tabela referente a essa classe que ta la no core/models
    #session.query(User).all() = "Select * from users"
    users = session.query(User).all()

    return render_template('core/users.html', lista_users=users)


#Esse código comentado é de dudu mas n tem nada dmais não
# @core.route('/dashboard')
# @login_required
# def dash():
#     return render_template('core/index.html')