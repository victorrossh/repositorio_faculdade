lista = []
count = 0
while count <2:
    x = int(input("Digite a quantidade total no estoque: "))
    lista.append(x)
    count+=1

x = sum(lista)
y = len(lista)
media = x/y

maior = max(lista)

print(maior)    
print(media)