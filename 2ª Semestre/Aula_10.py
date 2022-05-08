'''
1 - Herança Múltipla
'''

class Estudante:

    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    

class Funcionario:

    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario


class Monitor(Estudante, Funcionario):

    def __init__(self,nome, matricula, curso, salario, disciplina, carga_horaria):
        Estudante.__init__(self, nome, matricula, curso)
        Funcionario.__init__(self, nome, salario)
        self.__disciplina = disciplina
        self.__carga_horaria = carga_horaria
    
    def get_disciplina(self):
        return self.__disciplina
    
    def get_carga_horaria(self):
        return self.__carga_horaria
    
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina
    
    def set_carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria
    


estudante = Estudante("Maria", 456789, "ADS")
funcionario = Funcionario("João", 2000)
monitor = Monitor("Paulo", 123456, "SI", 1000.0, "POO", 4)

print(f"Nome: {monitor.nome}")                            # Paulo
print(f"Matricula: {monitor.matricula}") #, monitor.matricula)                  # 123456
print("Curso:", monitor.curso)                          # SI
print("Salario:", monitor.salario)                      # 1000.0
print("Disciplina:", monitor.get_disciplina())          # POO
print("Carga Horaria:", monitor.get_carga_horaria())    # 4
print("------------------------------------------------")

'''
2
'''


class Pessoa:

    def __init__(self, nome, endereco, fone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf
    

class Aluno(Pessoa):

    def __init__(self, nome, endereco, fone, cpf):
        super().__init__(nome, endereco, fone, cpf)
        self.disciplina = []
    
    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)

class Disciplina:

    def __init__(self, nome):
        self.nome = nome


class Funcionario(Pessoa):

    def __init__(self, nome, endereco, fone, cpf, salario):
        super().__init__(nome, endereco, fone, cpf)
        self.salario = salario


class Professor(Funcionario):

    def __init__(self, nome, endereco, fone, cpf, salario, titulacao):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.titulacao = titulacao
        self.disciplina = []

    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)

class Tecnico(Funcionario):

    def __init__(self, nome, endereco, fone, cpf, salario, cargo):
        super().__init__(nome, endereco, fone, cpf,salario)
        self.cargo = cargo



disciplina1 = Disciplina("Programação")
disciplina2 = Disciplina("Banco de Dados")
professor1 = Professor("Joao", "Rua Silva, 456", "(11)99999-9555", "9999999", 2000, "Mestrado")
aluno1 = Aluno("Maria", "Avenida São Francisco, 239", "(11)98888-8435", "555555")
tecnico1 = Tecnico("Pedro", "Rua Rocha, 77", "(11)93333-3333", "8787887", 1500, "Tecnico")
 
aluno1.incluir_disciplina(disciplina1)
aluno1.incluir_disciplina(disciplina2)
professor1.incluir_disciplina(disciplina1)
 
print('Disciplinas associadas ao aluno:')
for x in aluno1.disciplina:
    print(x.nome)
 
print('Disciplinas associadas ao Professor:')
for x in professor1.disciplina:
    print(x.nome)



'''
3
'''

class Veiculo:

    def __init__(self, marca, modelo, rodas, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.__velocidade = velocidade

    def get_velocidade(self):
        return self.__velocidade
    
    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade
    
    def acelerar(self, valor):
        self.__velocidade =+ valor
    
    def frear(self, valor):
        self.__velocidade -= valor


class Automovel(Veiculo):

    def __init__(self,marca, modelo, rodas, potencia):
        super().__init__(marca, modelo, rodas)
        self.potencia = potencia


class Bicicleta(Veiculo):

    def __init__(self, marca, modelo, rodas, marcha, bagageiro):
        super().__init__(marca, modelo, rodas)
        self.marcha = marcha
        self.bagageiro = bagageiro

    def imprimir_informacoes(self):
        print("----------------------------------------------------------------")
        print(f"Marca da Bike: {self.marca}")
        print(f"Modelo da Bike: {self.modelo}")
        print(f"Rodas da Bike: {self.rodas}")
        print(f"Marchas da Bike: {self.marcha}")
        return self.bagageiro

class Carro(Automovel):

    def __init__(self, marca, modelo, rodas, potencia, porta):
        super().__init__(marca, modelo, rodas, potencia)
        self.porta = porta

    
    def imprimir_informacoes(self):
        print("----------------------------------------------------------------")
        print(f"Marca do carro: {self.marca}")
        print(f"Modelo do carro: {self.modelo}")
        print(f"Rodas do carro: {self.rodas}")
        print(f"Potência do carro: {self.potencia}")
        print(f"Portas do carro: {self.porta}")


class Moto(Automovel):

    def __init__(self, marca, modelo, rodas, potencia, partida_eletrica):
        super().__init__(marca, modelo, rodas, potencia)
        self.partida_eletrica = partida_eletrica
    
    def imprimir_informacoes(self):
        print("----------------------------------------------------------------")
        print(f"Marca da moto: {self.marca}")
        print(f"Modelo da moto: {self.modelo}")
        print(f"Rodas da moto: {self.rodas}")
        print(f"Potência da moto: {self.potencia}")
        return self.partida_eletrica



carro = Carro("Ford", "Ka", 4, 85.0, 5)
moto = Moto("Honda", "Biz", 2, 9.2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)
 
carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)
 
carro.imprimir_informacoes()   # imprime os valores de todos os atributos do carro
bike.imprimir_informacoes()    # imprime os valores de todos os atributos da bicicleta
moto.imprimir_informacoes()    # imprime os valores de todos os atributos da moto
 
# testar a velocidade atual
print("----------------------------------------------------------------")
print("Velocidade atual do Carro:", carro.get_velocidade())       # 20
print("Velocidade atual da Moto:", moto.get_velocidade())         # 80
print("Velocidade atual da Bicicleta:", bike.get_velocidade())    # 15