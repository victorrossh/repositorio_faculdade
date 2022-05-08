import ac02_teste


class Socio:
    def __init__(self, nome, nascimento, cpf, mes, ano):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.mes = mes
        self.ano = ano


class Clube:
    def __init__(self):
        self.socios = []

    def associar(self, socio):
        self.socios.append(socio)
        return self.socios

    def numero_de_socios(self):
        n_socios = len(self.socios)
        return n_socios

    def mes_associacao(self, mes, ano):
        self.ano = ano
        self.mes = mes
        cont = 0
        if self.mes > 12 or self.mes < 1:
            raise ValueError
        if len(str(self.ano)) != 4:
            raise TypeError
        for socio in self.socios:
            dicio = socio.__dict__
            if dicio["mes"] == self.mes and dicio["ano"] == self.ano:
                cont += 1
        return cont

    def expulsar(self, mes, ano):
        self.ano = ano
        self.mes = mes
        lista = []
        manter = []
        if self.mes > 12 or self.mes < 1:
            raise ValueError
        if len(str(self.ano)) != 4:
            raise TypeError
        for socio in self.socios:
            if socio.mes == self.mes and socio.ano == self.ano:
                lista.append(socio.nome)
            else:
                manter.append(socio)
        self.socios = manter
        lista.sort()
        tupla = tuple(lista)
        return tupla
