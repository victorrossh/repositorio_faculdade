import random
lista = []
lista_par = []
lista_impar = []

for i in range(10):
    lista.append(int(input("Digite um número: ")))
    print("Lista", lista)
for x in lista:
    if x % 2 == 0:
        print("Lista", lista_par)
    else:
        print("Lista", lista_impar)