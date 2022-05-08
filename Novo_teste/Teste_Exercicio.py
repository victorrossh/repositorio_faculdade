class Livro:

    def titulo(self, titulo, autor, quantidade_paginas):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas




class Triangulo:


    med1 = int(input("Lado A: "))
    med2 = int(input("Lado B: "))
    med3 = int(input("Lado C: "))

    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        self.calculo = self.lado_a + self.lado_b + self.lado_c
        print(f"O valor do perímeto é {self.calculo}")


medida = Triangulo(med1, med2, med3)

class Televisao:

    def __init__(self, canal=None, volume=0):
        self.canal = canal
        self.volume = volume
    
    def aumentar_volume(self):
        volume +=1

    def diminuir_volume(self):
        volume -=1

    def alterar_canal(self, canal):
        self.canal = canal

tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f"A tv está no canal {tv.canal}")
print(f"A tv está no volume {tv.volume}")


class funcionário:

    def __init__(self, nome=None, salario=0):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.aumento = self.salario*(percentual/100+1)
        print(f"{self.nome} receberá de salário {self.aumento}")


    nome = input("Nome: ")
    salario = float(input("Salario: "))
    percentual = float(input("Percentual: "))

trabalhador = Funcionario(nome, salario)
trabalhador.aumentar_salario(percentual)