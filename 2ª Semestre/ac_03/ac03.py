# ATIVIDADE CONTÍNUA 03

# NOMES DOS ALUNOS (máximo 6 alunos)
# ALUNO 1: Guilherme Da Silva Gonçalves RA: 1901291
# ALUNO 2: Ruan Klause Jurado Oliveira RA: 2100302
# ALUNO 3: Vitor Cabral da Silva RA: 2101210


class SuperPoder:

    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    
    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria


class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []

    def adicionar_super_poder(self, superpoder):
        if len(self.__poderes) == 4:
            raise ValueError
        else:
            self.__poderes.append(superpoder)
            

    def get_poder_total(self):
        soma_poderes = 0
        for x in self.__poderes:
            soma_poderes += SuperPoder.get_categoria(x)
        return soma_poderes


class SuperHeroi(Personagem):
    def get_poder_total(self):
        heroi = super().get_poder_total()*1.10
        return heroi


class Vilao(Personagem):

    def __init__(self,nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao


class Confronto:
    def lutar(self, heroi, vilao):
        if heroi.get_poder_total() > vilao.get_poder_total():
            return 1
        elif vilao.get_poder_total() > heroi.get_poder_total():
            return 2
        else:
            return 0