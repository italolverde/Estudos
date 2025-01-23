from sqlalchemy import create_engine, Table, Column, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, relationship
from typing import List

engine = create_engine('sqlite:///exemplo2.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

# studants_courses = Table(
#     'students_courses',
#     Base.metadata,
#     Column('students_counses', ForeignKey('studants.id'), primary_key=True),
#     Column('courses_id', ForeignKey('courses.id'), primary_key=True)
# )

#Relacionamento de 1:n

class Estudante(Base):
    __tablename__ = 'studants'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    curso_id:Mapped[int] = mapped_column(ForeignKey('courses.id'), nullable = True)
    def __repr__(self) -> str:
        return f"Estudantes: {self.nome}"

class Curso(Base):
    __tablename__ = 'courses'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    estudantes:Mapped[List['Estudante']] = relationship('Estudante', backref='curso')
    def __repr__(self) -> str:
        return f"Curso: {self.nome}"


Base.metadata.create_all(bind=engine)
info = Curso(nome='Informática')

x = Estudante(nome = 'Popo', curso_id=1)
y = Estudante(nome = 'Ruan', curso_id=1)
z = Estudante(nome = 'Sebosao')

# session.add(info)
# session.add_all([x,y,z])
# session.commit()

#SELECT * FROM courses WHERE id = 1
curso = session.query(Curso).get(1)
print(curso) #"Curso: Informática"
print(curso.estudantes) #[Estudante: Popo, Estudante: Ruan]

estudante = session.query(Estudante).get(1)
print(f"Curso de {estudante}: {estudante.curso}")