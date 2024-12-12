from sqlalchemy import create_engine,text
from sqlalchemy.orm import Session
from database.models import Base,User
from faker import Faker
engine = create_engine('sqlite:///teste.db')
session = Session(bind=engine)

fake = Faker()

def start_db():
    Base.metadata.create_all(bind=engine)
    for _ in range(100):
        fake_name = fake.unique.name()
        user = User(name=fake_name)
        session.add(user)
        session.commit()

#listar todos os usuarios
#session.query(User).where(User.name.startswith('R')) RETORNA UMA LISTA



def destroy_db():
    Base.metadata.drop_all(bind=engine)




