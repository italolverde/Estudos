from sqlalchemy import create_engine, Table, Column, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, relationship
from typing import List

engine = create_engine('sqlite:///exemplo1.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

studants_courses = Table(
    'students_courses',
    Base.metadata,
    Column('students_counses', ForeignKey('studants.id'), primary_key=True),
    Column('courses_id', ForeignKey('courses.id'), primary_key=True)
)

#Relacionamento de n:n

class Estudante(Base):
    __tablename__ = 'studants'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    #Back_populates: Nome do atributo que você vai chamar no objeto da outra tabela || exemplo: curso.ESTUDANTES
    #secondary: nome da tabela intermediária
    cursos:Mapped[List['Curso']] = relationship('Curso', secondary=studants_courses, back_populates='estudantes')

class Curso(Base):
    __tablename__ = 'courses'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    #Back_populates: Nome do atributo que você vai chamar no objeto da outra tabela || exemplo: curso.ESTUDANTES
    #secondary: nome da tabela intermediária
    estudantes = relationship('Estudante', secondary=studants_courses, back_populates='cursos')

Base.metadata.create_all(bind=engine)

info = Curso(nome='Informática')
x = Estudante(nome = 'Popo')
y = Estudante(nome = 'Ruan')
z = Estudante(nome = 'Sebosao')

session.add(info)
session.add_all([x,y,z])

session.commit()

info = session.query(Curso).get(1)
info.estudantes.append(x)
session.commit()