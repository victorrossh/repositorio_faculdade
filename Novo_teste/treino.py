from abc import ABC


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
            print("Saldo insuficiente")

    def consultar_saldo(self):
        print("Saldo: ", self.saldo)


class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass


class ContaCorrenteEspecial(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):                     # polimorfismo de inclusão
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo + Limite insuficientes")


contacorrente = ContaCorrente(123, "Paulo", 100)
contaespecial = ContaCorrenteEspecial(555, "Paulo", 200, 300)
contapoupanca = ContaPoupanca(333, "João", 0)

contacorrente.sacar(100)
contaespecial.sacar(100)
contapoupanca.sacar(100)

contacorrente.consultar_saldo()
contaespecial.consultar_saldo()
contapoupanca.consultar_saldo()