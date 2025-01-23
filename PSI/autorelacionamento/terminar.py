from sqlalchemy import create_engine, Table, Column, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, relationship
from typing import List

engine = create_engine('sqlite:///exemplo1.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

class Paciente(Base):
    __tablename__ = 'pacientes'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[int]
    medicos:Mapped[List['Medico']] = relationship('Medico', secondary='Consulta', back_populates='pacientes')

class Medico(Base):
    __tablename__ = 'medicos'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[int]
    pacientes = relationship('Paciente', secondary='Consulta', back_populates='medicos')

class Consulta(Base):
    __tablename__ = 'consultas'
    id:Mapped[int] = mapped_column(primary_key=True)
    paciente_id:Mapped[int] = mapped_column(ForeignKey('pacientes.id'), nullable = True)
    medico_id:Mapped[int] = mapped_column(ForeignKey('medicos.id'), nullable = True)


