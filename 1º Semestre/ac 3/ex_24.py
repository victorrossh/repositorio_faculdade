x = 0
soma_tempo = 0
lista = []
anual = 0
while x <5:
    clima = int(input("Digite a temperatura da sua cidade: "))
    lista.append(clima)
    soma_tempo +=clima
    x+=1
media = soma_tempo/len(lista)
maximo = max(lista)
minimo = min(lista)

for x in lista:
    if x <media:
        anual +=1
print(f"A maior temperatura do ano foi de {maximo} graus Celsius e a menor foi {minimo}. E o número de dias que a temperatura foi abaixo da média foi de {anual}. ")