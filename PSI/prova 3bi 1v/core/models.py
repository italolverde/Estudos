from flask_login import UserMixin
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

class Base(DeclarativeBase):
    pass 

class User(Base,UserMixin):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str]
    nome:Mapped[str]
    senha:Mapped[str]
    
    def get_id(self):
        return self.id

    def __init__(self, nome,email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha