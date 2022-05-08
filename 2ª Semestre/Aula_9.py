'''
1 - Herança
'''


class Pessoa:

    def __init__(self, identificador, nome):
        self. identificador = identificador
        self.nome = nome


class PessoaJuridica(Pessoa):

    def __init__(self, identificador, nome, cnpj):
        super().__init__(identificador, nome)
        self.cnpj = cnpj


class PessoaFisica(Pessoa):

    def __init__(self, identificador, nome, rg, cpf):
        super().__init__(identificador, nome)
        self.rg = rg
        self.cpf = cpf


pessoa1 = Pessoa(1, "Nome da Pessoa")
p_juridica = PessoaJuridica(2, "Nome da Pessoa Juridica", "1111111111")
p_fisica = PessoaFisica(3, "Nome da Pessoa Fisica", "222222222", "333333333")

print(pessoa1.identificador)        # 1
print(pessoa1.nome)                 # Nome da Pessoa

print(p_juridica.identificador)     # 2
print(p_juridica.nome)              # Nome da Pessoa Juridica
print(p_juridica.cnpj)              # 1111111111

print(p_fisica.identificador)       # 3
print(p_fisica.nome)                # Nome da Pessoa Fisica
print(p_fisica.rg)                  # 222222222
print(p_fisica.cpf)                 # 333333333


'''
2
'''


class Animal:

    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas

    def exibir_dados(self):
        print(f"Nome do animal: {self.nome}.")
        print(f"Cor: {self.cor}.")
        print(f"Patas: {self.numero_patas}.")


class Cachorro(Animal):

    def __init__(self, nome, cor, numero_patas, raça):
        super().__init__(nome, cor, numero_patas)
        self.raça = raça

    def exibir_dados(self):
        print(f"Nome do animal: {self.nome}.")
        print(f"Cor: {self.cor}.")
        print(f"Patas: {self.numero_patas}.")
        print(f"Raça: {self.raça}")


animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados()

dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados()

'''
3
'''


class Imovel:

    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco


class ImovelNovo(Imovel):

    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def calcular_preco(self):
        self.preco = self.adicional + self.preco
        return self.preco


class ImovelVelho(Imovel):

    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def calcular_preco(self):
        self.preco = self.preco - self.desconto
        return self.preco


imovel = Imovel("Rua Silva, 123", 300000.0)
imovel_novo = ImovelNovo("Rua Joaquim, 999", 250000.0, 20000.0)
imovel_velho = ImovelVelho("Av. Brasil, 777", 500000.0, 35000.0)

print(imovel.endereco)                                      # Rua Silva, 123
print('Preço:', imovel.preco)                               # 300000.0

print(imovel_novo.endereco)                                 # Rua Joaquim, 999
print('Preço:', imovel_novo.preco)                          # 250000.0
print('Preço Atualizado:', imovel_novo.calcular_preco())    # 270000.0

print(imovel_velho.endereco)                                # Av. Brasil, 777
print('Preço:', imovel_velho.preco)                         # 500000.0
print('Preço Atualizado:', imovel_velho.calcular_preco())   # 465000.0


'''
4
'''


class Motor:

    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia


class Veiculo:

    def __init__(self, ano, veiculo, motor):
        self.ano = ano
        self.veiculo = veiculo
        self.motor = motor

    def exibir_dados(self):
        print("--------------------------------------------------------")
        print(f"Ano do veiculo: {self.ano}")
        print(f"Veiculo: {self.veiculo}")
        print(f"motor: {self.motor}")
        print(f"Cilindrada: {self.motor.cilindrada}")
        print(f"Potência: {self.motor.potencia}")


class Carro(Veiculo):

    def __init__(self, ano, veiculo, motor, cor, modelo):
        super().__init__(ano, veiculo, motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cor: {self.cor}")
        print(f"Modelo: {self.modelo}")


class Caminhao(Veiculo):

    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Comprimento: {self.comprimento}")


motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)

carro.exibir_dados()
caminhao.exibir_dados()
