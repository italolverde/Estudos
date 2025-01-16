from sqlalchemy.orm import Mapped, mapped_column
from database import db

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]

class Livros(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]