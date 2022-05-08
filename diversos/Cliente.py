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

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo += valor
        else:
            print("senha invalida")

    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo -= valor
        else:
            print("senha invalida")


cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print(conta.get_saldo())
conta.sacar(50, "123")
print(conta.get_saldo())

conta.depositar(100, "111")
print(conta.get_saldo())
conta.sacar(50, "111")
print(conta.get_saldo())