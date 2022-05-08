lista = []
count = 10

for i in range (10):
    var1 = int(input("Digite um número: "))
    lista.append(var1)

    maior = max (lista)
    media = sum (lista)/len(lista)

    print(lista)
    print(media)

