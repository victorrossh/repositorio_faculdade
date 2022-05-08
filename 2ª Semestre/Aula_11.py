from abc import ABC, abstractmethod
'''
1
'''

class Operaçao(ABC):

    @abstractmethod
    def calcular(self, x, y):
        pass


class Soma(Operaçao):

    def calcular(self, x , y):
        return x + y


class Subtracao(Operaçao):

    def calcular(self, x , y):
        return x - y


class Multiplicacao(Operaçao):

    def calcular(self, x , y):
        return x * y


class Divisao(Operaçao):

    def calcular(self, x, y):
        return x / y


soma = Soma()
sub = Subtracao()
div = Divisao()
mult = Multiplicacao()

print(soma.calcular(10, 5))
print(sub.calcular(10, 5))
print(div.calcular(10, 5))
print(mult.calcular(10, 5))

print("------------------------------------")

'''
2
'''

class Animal(ABC):

    def __init__(self, nome , idade):
        self. nome = nome
        self. idade = idade


class Veterinario:

    @abstractmethod
    def examinar(self, animal):
        pass


class Cachorro(Animal):

    def emitir_som(self):
        print("Cachorro Latiu")
    

class Gato(Animal):

    def emitir_som(self):
        print("Miau")


class Cavalo(Animal):

    def emitir_som(self):
        print("Cavalo Relinchou")



dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato

print("------------------------------------")

'''
3
'''

class Funcionario(ABC):

    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base
        
        
    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):

    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
        
    def calcular_salario(self):
        return self.salario_base * 2


class Assistente(Funcionario):

    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
    
    def calcular_salario(self):
        return self.salario_base


class Vendendor(Funcionario):

    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
    
    def calcular_salario(self):
       return (self.salario_base*10)/ 100 + self.salario_base


gerente = Gerente("Vitor", 123456, 8500)
vendendor = Vendendor("João", 14789, 2000)
assistente = Assistente("Rafael", 15699, 1800)


lista = [gerente, vendendor, assistente] 

print("Os salário dos funcionários foram atribuidos na lista.")
for x in lista:
    print(f"Salario: {x.calcular_salario()}")

print("------------------------------------")

'''
4
'''

class Conta(ABC):

    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo: {self.saldo}")



class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

class ContaEspecial(Conta):
    
    def __init__(self, nome, titular, saldo, limite):
        super().__init__(nome, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo + Limite insuficientes.")



contacorrente = ContaCorrente(123 , "Vitor Cabral", 100)
contaespecial = ContaEspecial(456, "Rafael", 250, 500)
contapoupanca = ContaPoupanca(789, "Gisele", 0)

contacorrente.sacar(80)
contaespecial.sacar(100)
contapoupanca.sacar(100)

contacorrente.consultar_saldo()
contaespecial.consultar_saldo()
contapoupanca.consultar_saldo()