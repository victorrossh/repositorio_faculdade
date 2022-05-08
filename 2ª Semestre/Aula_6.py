class Carro:

    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")


meu_carro = Carro("Nissan", "GTR R-35", 1234)
meu_carro.exibir_dados()


class Funcionario:

    def __init__(self, nome, sobrenome, salario_mensal):
        if salario_mensal < 0:
            self.salario_mensal = 0
        else:
            self.salario_mensal = salario_mensal

        self.nome = nome
        self.sobrenome = sobrenome

    def aumentar_salario(self):
        salario = self.salario_mensal*10/100
        self.salario_mensal += salario
        return self.salario_mensal
        
    def salario_anual(self):
        return self.salario_mensal * 12


trabalhador = Funcionario("Vitor", "Cabral", 1500)
trabalhador.salario_anual()
trabalhador.aumentar_salario()

print(trabalhador.nome)
print(trabalhador.sobrenome)
print(trabalhador.salario_anual())
print(trabalhador.aumentar_salario())


class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0

    def depositar(self, valor, senha):

        if senha == self.senha:
            self.saldo += valor
            print("Operação realizada com sucesso.")
        else:
            print("Não foi possível realizar o deposito")

    def sacar(self, valor, senha):

        if senha == self.senha:
            self.saldo -= valor
            print("Operação realizada com sucesso.")
        else:
            print("Não foi possível realizar o saque")


conta1 = ContaBancaria(6587, "Vitor Cabral", 123456)

valor = float(input("Valor para deposito: "))
senha = int(input("Informe a senha: "))
conta1.depositar(valor, senha)
print(f"Saldo: {conta1.saldo}")


valor = float(input("Valor para saque: "))
senha = int(input("Informe a senha: "))
conta1.sacar(valor, senha)
print(f"Saldo:  {conta1.saldo}")


class Aluno:

    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []

    def inserir_notas(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        media = sum(self.notas)/len(self.notas)
        return media


aluno1 = Aluno(123456, "Vitor Cabral", "EC - 2A")
aluno2 = Aluno(567654, "Eduardo", "EC - 2A")
aluno3 = Aluno(789466, "Weverton", "EC - 2B")

aluno1.inserir_notas(8)
aluno1.inserir_notas(7)
aluno1.inserir_notas(6)

aluno2.inserir_notas(10)
aluno2.inserir_notas(5)
aluno2.inserir_notas(2)

aluno3.inserir_notas(8)
aluno3.inserir_notas(8)
aluno3.inserir_notas(8)

lista = [aluno1, aluno2, aluno3]

for aluno in lista:
    print(aluno.nome, aluno.calcular_media())

