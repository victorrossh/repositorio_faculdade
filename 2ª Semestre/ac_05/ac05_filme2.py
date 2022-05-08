from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import Function
engine = create_engine("sqlite:///server.db")
connection = engine.connect()


session = Session()

Base = declarative_base(engine)

class Filme(Base):

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


class BancoDeDados:
    def criar_tabela(self):

        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                              ID INTEGER PRIMARY KEY,
                              TITULO VARCHAR(255),
                              ANO INT,
                              DIRECAO VARCHAR(255),
                              GENERO VARCHAR(255),
                              UF VARCHAR(255),
                              PRODUTORA VARCHAR(255),
                              RENDA FLOAT,
                              PUBLICO INT)""")

    def incluir(self, filme):

        session.add(filme)
        session.commit()

    def incluir_lista(self, filmes):

        session.add_all(filmes)
        session.commit()

    def incrementar_renda(self, id_filme, valor):

       resultado = session.query(Filme).get(id_filme)
       if resultado is not None:
           resultado += valor
           session.commit()

    def excluir(self, id_filme):

        resultado = session.query(Filme).get(id_filme)
        if resultado is not None:
            session.delete(resultado)
            session.commit()

    def buscar_todos(self):

        lista = []
        resultado = session.query(Filme)
        for x in resultado:
            lista.append(x)
        return lista

    def buscar_por_ano(self, ano):

        lista = []
        resultado = session.query(Filme).filter(Filme.ano == ano).order_by(Filme.titulo)
        for x in resultado:
            lista.append(x)
        return lista

    def buscar_por_genero(self, genero):

        lista = []
        resultado = session.query(Filme).filter(Filme.genero.like('%' + genero + '%')).order_by(Filme.distribuidora)
        for filme in resultado:
            lista.append(filme)
        return lista


    def buscar_por_direcao(self, diretor):
        lista = []
        resultado = session.query(Filme).filter(Filme.direcao.like('%' + diretor + '%')).order_by(Filme.titulo)
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
        with open(nome_arquivo, 'r', encoding='UTF - 8') as arquivo:
            filmes = []
            for linha in arquivo:
                linha = linha.split(';')
                filme = Filme(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8])
                filmes.append(filme)
            session.add_all(filme)
            session.commit()

    def exportar_filmes(self, nome_arquivo):
        with open(nome_arquivo, 'r', encoding='UTF - 8') as arquivo:
            resultado = session.query(Filme)
            for resultado in resultado:
                arquivo.write(str(resultado.ano)+';' + resultado.titulo +
                              ';' + resultado.direcao+';'+resultado.genero+';'+resultado.produtora +';'+resultado.distribuidora+';'+str(resultado.publico)+';'+str(resultado.renda) + '\n')

# =============================================================================
# EXEMPLO DE PROGRAMA PRINCIPAL

# Instância da classe Banco de Dados
banco = BancoDeDados()

# Cria a tabela Filme
banco.criar_tabela()

# Importa filmes do arquivo de texto e salva no banco de dados
banco.importar_filmes('movies.txt')


print('-'*50)
lista = banco.buscar_todos()
for f in lista:
    print(f.id, f.titulo, f.ano, f.direcao, f.genero, f.uf, f.produtora,
          f.renda, f.publico)

print('-'*50)
lista = banco.buscar_por_ano(2018)
for f in lista:
    print(f.id, f.titulo, f.ano, )

print('-'*50)
lista = banco.buscar_por_genero('Ficção')
for f in lista:
    print(f.id, f.titulo, f.ano, f.genero)

print('-'*50)
lista = banco.buscar_por_direcao('Fernando Meirelles')
for f in lista:
    print(f.id, f.titulo, f.ano, f.direcao)


print('-'*50)
lista = banco.buscar_por_renda()
for f in lista:
    print(f.id, f.titulo, f.ano, f.renda)


print('-'*50)
f = banco.buscar_menor_publico()
print(f.id, f.titulo, f.ano, f.publico)


filme1 = Filme('O Brasileiro', 2019, 'Julio Bressane', 'Ficção','RJ', 'Julio Bressane', 50000, 4616)
banco.incluir(filme1)

filme2 = Filme('O Fim do Fim', 2007, 'Beto Magalhães/Cao Guimarães',
               'Documentário', 'RJ', 'Bananeira Filmes', 9821, 1170)
filme3 = Filme('Sambando nas Estrelas', 2009, 'Elizeu Ewald', 'Documentário',
               'RJ', 'E.S. Comunicações', 8971, 3071)
lista_filmes = [filme2, filme3]
banco.incluir_lista(lista_filmes)


banco.incrementar_renda(700, 500.0)


banco.excluir(600)

banco.exportar_filmes('saida.txt')
