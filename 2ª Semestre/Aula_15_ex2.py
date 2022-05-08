from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///server2.db")

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

arquivo = open('funcionarios.txt', 'r', encoding='UTF-8')

lista_funcionario = []

for linha in arquivo:
    lista = linha.split(';') # separa os dados - split.
    func = Funcionario(lista[0], int(lista[1]), float(lista[2]))
    lista_funcionario.append(func)


session.add_all(lista_funcionario)
session.commit()


resultado = session.query(Funcionario)
for x in resultado:
    print(x.id, x.nome, x.idade, x.salario)

arquivo.close()
connection.close()