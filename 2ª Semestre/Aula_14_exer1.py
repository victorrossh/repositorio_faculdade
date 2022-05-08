from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///cabral.db")
connection = engine.connect()

session = Session()

Base = declarative_base(engine)


connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INT,
                        SALARIO FLOAT)
                        """) 

class Funcionario(Base):
    __tablename__ = 'Funcionario'
    id = Column('ID', Integer, primary_key = True, autoincrement = True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


func = Funcionario("Vitor Cabral", 22, 2100)
session.add(func)
session.commit()


func1 = Funcionario("Rafael", 45, 500)
func2 = Funcionario("João", 22, 3800)
lista = [func1, func2]
session.add_all(lista)
session.commit()


#consulta dados
print("*" *30)
resultado = session.query(Funcionario)
for x in resultado:
    print(f"ID: {x.id}")
    print(f"NOME: {x.nome}")
    print(f"IDADE: {x.idade}")
    print(f"SALARIO: {x.salario}")

#consulta ultilizando filtro (salario)
print("*" *30)
resultado = session.query(Funcionario).filter(Funcionario.salario >1500)
for x in resultado:
    print(f"ID: {x.id}")
    print(f"NOME: {x.nome}")
    print(f"IDADE: {x.idade}")
    print(f"SALARIO: {x.salario}")
    
connection.close()
