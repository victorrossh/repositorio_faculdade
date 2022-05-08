class Cliente:

    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha
    
    def get_cpf(self):
        return self.__cpf

    def get_senha(self):
        return self.__senha

    def validar_senha(self, senha):
        if senha == self.__senha:
            return True
        else:
            print("Senha inválida")
            return False


class ContaBancaria:

    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = saldo

    def get_saldo(self, senha):
        if self.cliente.validar_senha(senha):
            return self.__saldo

    def sacar(self, valor, senha):
        if self.cliente.validar_senha(senha):
            self.__saldo -= valor

    def depositar(self, valor, senha):
        if self.cliente.validar_senha(senha):
            self.__saldo += valor


cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)
conta.depositar(200, "123")
print(conta.get_saldo(senha="123"))            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo(senha="123"))            # Imprime 150
conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo(senha="123"))            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo(senha="123"))            # Imprime 150