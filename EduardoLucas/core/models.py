from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from database import Base

class User(UserMixin, Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str] = mapped_column(String(50),unique=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    #Unique = True: Não podem ter valores repetidos, se tiver da erro
    senha: Mapped[str]
    #Confuso, mas é um auto relacionamento, ele cria uma chave estrangeira pra uma coluna da própria tabela
    #Mas tenho quase certeza que ele fez isso incompleto, desenvolvo no txt que deixei
    #nullable=True: é uma coluna sem o NOT NULL
    gerente_id:Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)

