lista = []
count = 10

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    

x = sum(lista)
y = len(lista)
media = x/y

print(lista)
print(F"A média dos números é {media}")