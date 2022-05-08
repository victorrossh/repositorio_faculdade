'''
1
'''


class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        self.__salario = novo_salario

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_nome(self, nome):
        self.__nome = nome


func1 = Funcionario("Pedro", "111222333-22", 1500.0)
func1.set_salario(2000.0)
print("Nome:", func1.get_nome())
print("CPF:", func1.get_cpf())
print("Salário:", func1.get_salario())


'''
2
'''


class Filme:

    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


lista = []

titulo1 = input("Nome do filme: ")
genero1 = input("Gênero do filme: ")
titulo2 = input("Nome do filme: ")
genero2 = input("Gênero do filme: ")
titulo3 = input("Nome do filme: ")
genero3 = input("Gênero do filme: ")

filme1 = Filme(titulo1, genero1)
filme2 = Filme(titulo2, genero2)
filme3 = Filme(titulo3, genero3)


lista.append(filme1)
lista.append(filme2)
lista.append(filme3)

for x in lista:
    print(x.get_titulo())
    print(x.get_genero())

'''
3
'''


class Cliente:

    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_senha(self):
        return self.__senha

class ContaBancaria:

    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0
        

    def get_saldo(self,):
        return self.__saldo
  
    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo -= valor
        else:
            print("Senha inválida")

    def depositar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo += valor
        else: 
            print("Senha inválida")


cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, 123)
print(conta.get_saldo())
conta.sacar(50, 123)
print(conta.get_saldo())
conta.depositar(100, 123)
print(conta.get_saldo())
conta.sacar(50, 111)
print(conta.get_saldo())


'''
4
'''


class CarroCorrida:

    def __init__(self, numero, piloto, velocidade_maxima):
        self.__numero = numero
        self.__piloto = piloto
        self.__velocidade_maxima = velocidade_maxima
        self.__velocidade_atual = 0
        self.__ligado = False

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False

    def acelerar(self, velocidade):
        if self.__velocidade is True:
            self.__velocidade_atual += velocidade
            if self.__velocidade_atual > self.__velocidade_maxima:
                self.__velocidade_atual = self.__velocidade_maxima

    def frear(self):
        self.__velocidade_atual = 0

    def get_velocidade_atual(self):
        return self.__velocidade_atual == self.__velocidade_atual


carro = CarroCorrida(44, "Lewis Hamilton", 250)
carro.acelerar(280)
print(carro.get_velocidade_atual())

carro.ligar()
carro.acelerar(280)
print(carro.get_velocidade_atual())

carro.acelerar(20)
print(carro.get_velocidade_atual())

carro.frear()
print(carro.get_velocidade_atual())





