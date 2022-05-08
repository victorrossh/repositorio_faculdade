'''
Exercício 01 - Classe Livro
Implemente a classe Livro, conforme o diagrama a seguir. No programa principal e crie dois objetos da classe Livro.
- Atributo (titulo, autor, quantidade_paginas)
'''


class Livro:

    def titulo(self, titulo):
        print(f"O titulo do livro é {titulo}.")

    def autor(self, autor):
        print(f"O autor do livro é {autor}.")

    def quantidade_paginas(self, quantidade_paginas):
        print(f"A quantidade de páginas é {quantidade_paginas}.")


livro1 = Livro()
livro1.titulo("Harry Potter e a Pedra Filosofal")
livro1.autor("J. K. Rowling")
livro1.quantidade_paginas(264)
livro2 = Livro()
livro2.titulo("Poeira em alto mar")
livro2.autor("Alan Bida")
livro2.quantidade_paginas(100)


'''
Exercício 02 - Classe Triangulo
Crie uma classe que representa um triângulo.
Atributos:
lado_a
lado_b
lado_c

Métodos:
calcular_perimetro: retorna o perímetro do triângulo (soma dos três lados).

Crie um programa que utilize esta classe. O programa deve pedir ao usuário que informe as medidas dos três lados de um triângulo. Depois deve criar um objeto com essas medidas e exibir seu perímetro.
'''


class Triangulo:

    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        self.calcular_perimetro()

    def calcular_perimetro(self):
        self.calcular = self.lado_a + self.lado_b + self.lado_c
        print(f"O perímetro do triângulo é {self.calcular}.")


med1 = int(input("Digite a primeira medida: "))
med2 = int(input("Digite a segunda medida: "))
med3 = int(input("Digite a terceira medida: "))
medida = Triangulo(med1, med2, med3)

'''
Exercício 03 - Classe Televisão
Implemente a classe Televisao.
Atributos:
canal (o canal inicial da tv deve ser None)
volume (o volume inicial da tv deve ser zero)

Métodos:
aumentar_volume: aumenta o nível de volume em uma unidade.
diminuir_volume: diminui o nível de volume em uma unidade.
alterar_canal: recebe o número do canal que será sintonizado e altera o canal da tv.

Faça um programa para criar um objeto da classe Televisao e testar a sua classe.

'''


class Televisao:

    def __init__(self, canal=None, volume=0):
        self.canal = canal
        self.volume = volume

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal


tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f"A Tv está no volume {tv.volume}.")
print(f"O canal da tv é a {tv.canal}.")


'''
Exercício 04 - Classe Funcionário
Implemente uma classe Funcionario. 
tributos:
nome
salario

Métodos:
aumentar_salario: recebe como parâmetro de entrada um percentual e altera o salário do funcionário, de acordo com o percentual recebido.

Crie um programa que utilize esta classe. 
Ele deve pedir ao usuário o nome e o salário do funcionário e criar um objeto da classe Funcionario. Depois, deve solicitar ao usuário o percentual de aumento e executar o método aumentar_salario. Na sequência deve imprimir o salário do funcionário atualizado.

'''


class Funcionario:

    def __init__(self, nome=None, salario=0):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, aumento):
        self.salario = self.salario*(aumento/100+1)
        print(f"O funcionário {self.nome} terá um aumento e seu sálario é de R${self.salario}")




nome = input("NOME: ")
salario = float(input("Salário: "))
percentual = int(input("Percentual: "))

trabalhador = Funcionario(nome, salario)
trabalhador.aumentar_salario(percentual)


'''
Exercício 05 - Classe Carro
Implemente uma classe Carro
Atributos:
quantidade_combustivel (quantidade de litros de combustível no tanque do carro): a  quantidade inicial deve ser zero.

Métodos:
adicionar_combustivel: recebe uma quantidade de litros de combustível para abastecer o tanque.
obter_combustivel: retorna a quantidade atual de combustível.
andar: recebe uma distância em km e simula o ato de dirigir o veículo por essa distância, reduzindo o nível de combustível no tanque de gasolina. Considere que o veiculo consome 0.20 litros de combustivel por quilômetro percorrido.

Faça um programa para testar a classe Carro. Veja abaixo um trecho de programa que utiliza a classe:

'''


class Carro:

    def __init__(self, quantidade_combustivel=0):
        self.quantidade_combustivel = quantidade_combustivel

    def adicionar_combustivel(self, litros):
        self.quantidade_combustivel += litros

    def obter_combustivel(self):
        return self.quantidade_combustivel

    def andar(self, distancia):
        self.quantidade_combustivel -= (distancia*0.20)


meu_carro = Carro()
meu_carro.adicionar_combustivel(20)
meu_carro.andar(80)
print('Litros de combustível no tanque:', meu_carro.obter_combustivel())