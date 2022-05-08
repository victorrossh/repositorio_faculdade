'''
1
'''


class Pessoa:
    def __init__(self, nome, idade, carro):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def comprar_carro(self, carro):
        self.carro = carro


class Carro:

    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano


meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25, meucarro)
eu.comprar_carro(meucarro)
print(f"Meu nome: {eu.nome}")
print(f"Modelo do meu carro: {eu.carro.modelo} ")
print(f"Placa do meu carro: {eu.carro.placa} ")
print(f"Ano do carro: {eu.carro.ano}")


'''
2
'''


class Pedido:

    def __init__(self):
        self.produto = []

    def adicionar_produto(self, produto):
        self.produto.append(produto)

    def calcular_valor(self):
        total = 0
        for x in self.produto:
            total += (x.preco*x.quantidade)
        return total


class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor())

'''
3
'''


class Carro:

    def __init__(self, pneu1, pneu2, pneu3, pneu4):
        self.ligado = False
        self.pneu1 = pneu1
        self.pneu2 = pneu2
        self.pneu3 = pneu3
        self.pneu4 = pneu4
    
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False
    
    def verificar_pneu(self):
        if self.ligado is True:
            print(f"Pneu1: {self.pneu1.pressao}")
            print(f"Pneu2: {self.pneu2.pressao}")
            print(f"Pneu3: {self.pneu3.pressao}")
            print(f"Pneu4: {self.pneu4.pressao}")
        else:
            print("Carro desligado")


class Pneu:

    def __init__(self, pressao):
        self.pressao = pressao
    
    def furar(self):
        self.furar = 0


p1 = Pneu(32)
p2 = Pneu(32)
p3 = Pneu(36)
p4 = Pneu(36)
meucarro = Carro(p1, p2, p3, p4)
meucarro.ligar()
meucarro.pneu3.furar()
meucarro.verificar_pneu()
meucarro.desligar()
meucarro.verificar_pneu()

'''
4
'''


class Paciente:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self. idade = idade


class Medico:

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame:

    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_exame(self):
        print(f"Nome do paciente: {self.paciente.nome}")
        print(f"CPF: {self.paciente.cpf}")
        print(f"Idade: {self.paciente.idade}")
        print("---------------------------------------------")
        print(f"Nome do médico: {self.medico.nome}")
        print(f"CRM: {self.medico.crm}")
        print(f"Especialização: {self.medico.especializacao}")
        print("---------------------------------------------")
        print(f"Descrição: {self.descricao}")
        print(f"Resultado: {self.resultado}")


paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')
exame01.imprimir_exame()

'''
5
'''


class Emprego:

    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus


class Pessoa:

    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []

    def calcular_salario(self):
        porcentagem = len(self.dependentes) * self.emprego.bonus
        acrescimo = self.emprego.salario * porcentagem/100
        return self.emprego.salario + acrescimo


emprego = Emprego("Programador", "TI", 2000, 10)
pessoa1 = Pessoa("Vitor", "11-99999999", "vitor.cs11@email.com", emprego)

# dois dependentes (o dependente também é um objeto Pessoa)
dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

# adiciona dependentes na lista de dependentes da pessoa1
pessoa1.dependentes.append(dep1)
pessoa1.dependentes.append(dep2)

print("Salario: ", pessoa1.calcular_salario()) 
