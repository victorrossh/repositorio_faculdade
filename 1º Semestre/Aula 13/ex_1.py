lista = []
count = 10


for i in range (10): 
        var1 = lista.append(int(input("Digite um número: ")))

x = len(lista)
y = sum(lista)
media = y/x


print("Lista", lista, "\nmaior", max(lista),"\nmenor", min(lista))
print("Soma: ",sum(lista))
print("Média: ", media)

for z in lista:
    if z < media:
        print(z,end=' , .')