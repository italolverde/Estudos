from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db
from typing import List
from sqlalchemy import String, ForeignKey

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    livros: Mapped[List['Livros']] = relationship('Livros', backref='user')

class Livros(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id'))