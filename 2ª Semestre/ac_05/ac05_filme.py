# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS (máximo 6 alunos)
# ALUNO 1: Vitor Cabral da Silva RA:2101210
# ALUNO 2: Ruan Klause Jurado Oliveira RA:2100302
# ALUNO 3: Guilherme da Silva Gonçalves RA: 1901291
# ALUNO 4: Victor Ross RA:2100325
# ALUNO 5: Joao Pedro Souto Santos RA: 2101418
# ALUNO 6: Julian Oliveira Brandao RA: 2101891


# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)


# Classe para mapeamento da tabela
class Filme(Base):

    # FAZER O MAPEAMENTO DA TABELA
    _tablename_ = "FILME"
    id = Column('ID', Integer, primary_key=True)
    ano = Column('ANO', Integer)
    titulo = Column('TITULO', String(255))
    direcao = Column('DIRECAO', String(255))
    genero = Column('GENERO', String(255))
    produtora = Column('PRODUTORA', String(255))
    uf = Column('UF', String(255))
    distribuidora = Column('DISTRIBUIDORA', String(255))
    publico = Column('PUBLICO', Integer)
    renda = Column('RENDA', Float)

    # Método construtor

    def _init_(self, ano, titulo, direcao, genero, produtora, uf,
               distribuidora, publico, renda):
        self.ano = ano
        self.titulo = titulo
        self.direcao = direcao
        self.genero = genero
        self.produtora = produtora
        self.uf = uf
        self.distribuidora = distribuidora
        self.publico = publico
        self.renda = renda


# Classe para interação com o Banco de Dados
class BancoDeDados:
    def criar_tabela(self):

        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                              ID INTEGER PRIMARY KEY,
                              ANO INT,
                              TITULO VARCHAR(255),
                              DIRECAO VARCHAR(255),
                              GENERO VARCHAR(255),
                              PRODUTORA VARCHAR(255),
                              UF VARCHAR(255),
                              DISTRIBUIDORA VARCHAR(255),
                              PUBLICO INT,
                              RENDA FLOAT)""")

    def incluir(self, filme):
        session.add(filme)
        session.commit()

    def incluir_lista(self, filmes):
        session.add_all(filmes)
        session.commit()

    def incrementar_renda(self, id_filme, valor):
        resultado = session.query(Filme).get(id_filme)
        if resultado is not None:
            resultado.renda += valor
            session.commit()

    def excluir(self, id_filme):
        resultado = session.query(Filme).get(id_filme)
        if resultado is not None:
            session.delete(resultado)
            session.commit()

    def buscar_todos(self):
        lista = []
        resultado = session.query(Filme).order_by(Filme.ano)
        for filme in resultado:
            lista.append(filme)
        return lista

    def buscar_por_ano(self, ano):
        lista = []
        resultado = session.query(Filme).filter(
            Filme.ano == ano).order_by(Filme.titulo)
        for filme in resultado:
            lista.append(filme)
        return lista

    def buscar_por_genero(self, genero):
        lista = []
        resultado = session.query(Filme).filter(Filme.genero.like('%'+genero+'%')).order_by(Filme.distribuidora)
        for filme in resultado:
            lista.append(filme)
        return lista

    def buscar_por_direcao(self, diretor):
        lista = []
        resultado = session.query(Filme).filter(Filme.direcao.like('%'+diretor+'%')).order_by(Filme.titulo)
        for filme in resultado:
            lista.append(filme)
        return lista


    def buscar_por_renda(self):
        lista = []
        resultado = session.query(Filme).filter(Filme.renda > 1000000.0).order_by(Filme.renda)
        for filme in resultado:
            lista.append(filme)
        return lista

    def buscar_menor_publico(self):
        resultado = session.query(Filme).order_by(Filme.publico)
        return resultado[-1]

    def importar_filmes(self, nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            filmes = []
            for linha in arquivo:
                lista = linha.split(';')
                filme = Filme(lista[0], lista[1], lista[2], lista[3],lista[4], lista[5], lista[6], lista[7], lista[8])
                filmes.append(filme)
            session.add_all(filmes)
            session.commit()

    def exportar_filmes(self, nome_arquivo):
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            resultado = session.query(Filme)
            for resultado in resultado:
                arquivo.write(str(resultado.ano)+';' + resultado.titulo +
                              ';' + resultado.direcao+';'+resultado.genero+';'+resultado.produtora +';'+resultado.distribuidora+';'+str(resultado.publico)+';'+str(resultado.renda) + '\n')

