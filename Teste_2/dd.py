cont = 3
lista = []
for x in range(3):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if  x % 2 == 0:
        print(lista)
    else:
        print("Somente números pares.")


