from sqlalchemy import create_engine
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///sep.db")
connection = engine.connect()

session = Session()

Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(50)NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
                        ID INTEGER PRIMARY KEY,
                        TITULO VARCHAR(255) NOT NULL,
                        PAGINAS INT NOT NULL,
                        AUTOR_ID INT NOT NULL)""")

class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column("ID", Integer, primary_key = True, autoincrement = True)
    nome = Column("NOME", String(255))

    def __init__(self, nome):
        self.nome = nome

class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column("ID", Integer, primary_key = True, autoincrement = True)
    titulo = Column("TITULO", String(255))
    pagina = Column("Paginas", Integer)
    autor_id = Column("AUTOR_ID", Integer)

    def __init__(self, titulo, pagina, autor_id):
        #id = Não precisa estar no construtor
        self.titulo = titulo
        self.pagina = pagina
        self.autor_id = autor_id

autor1 = Autor("Vitor Cabral")
autor2 = Autor("Denílson")
lista = [autor1, autor2]
session.add_all(lista)
session.commit()


livro1 = Livro("Pequeno Príncipe", 255, 1)
livro2 = Livro("O Caneco de Prata", 300, 2)
lista2= [livro1,livro2]
session.add_all(lista2)
session.commit()

print("-"*30)
resultado = session.query(Autor)
for x in resultado:
    print(f"ID: {x.id}")
    print(f"NOME: {x.nome}")

print("-"*30)
resultado2 = session.query(Livro)
for y in resultado2:
    print(f"ID: {y.id}")
    print(f"TÍTULO: {y.titulo}")
    print(f"PÁGINA: {y.pagina}")
    print(f"AUTOR_ID: {y.autor_id}")

connection.close()
