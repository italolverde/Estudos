from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, relationship


engine = create_engine('sqlite:///exemplo1.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key = True)
    nome:Mapped[int]
    gerente_id:Mapped[int] = mapped_column(ForeignKey('users.id'), nullable = True)

Base.metadata.create_all(bind=engine)

user1 = User(nome='Seboso', gerente_id=1)
user2 = User(nome='Marquim', gerente_id=1)
user3 = User(nome='Ruan')
user4 = User(nome='Popo')
session.add(user4)
session.commit()

session.add_all([user1,user2,user3])
session.commit()
