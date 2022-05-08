from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///pl.db")

connection = engine.connect()

session = Session()

Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INTEGER,
                        SALARIO FLOAT)""")

class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

resultado = session.query(Funcionario).order_by(Funcionario.nome)

arquivo = open("saída.txt", "w", encoding="UTF-8")

for x in resultado:
    arquivo.write(x.nome + ';' + str(x.idade) + ';' + str(x.salario) + '\n')

arquivo.close()
connection.close()