from flask_login import LoginManager
from core.models import User
from database import session

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return session.get(User, user_id)

#Esse arquivo com essas funções confusas, esse negocio com @, é só comando de configuração, não tem o que aprofundar
#Aqui é ctrl+c e ctrl+v e aceitar que funciona, essa biblioteca n ta nem um pouco abstraida