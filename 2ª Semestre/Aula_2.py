'''
1) Preencha uma lista com 10 números digitados pelo usuário e exiba:
o maior número da lista
o menor número da lista
a quantidade de números pares contidos na lista
a média dos números contidos na lista
todos os números menores do que a média calculada no item anterior

'''

lista = []
lista_par = []
menor = 0
media = 0
for i in range(10):
    n = int(input("Digite um número: "))
    lista.append(n)

for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
print("Lista", lista_par)

for a in lista:
    if a < media:
        menor = menor + 1
print(f"Menores números do que a média {menor}.")



x = max(lista)
y = min(lista)
soma = sum(lista)
z = len(lista)
media = soma/z
print(f"O maior número é {x}.")
print(f"O menor número é {y}.")
print(f"A média é {media}.")

'''
2) Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista com os números pares e outra com os números ímpares. 

Exemplo: 
Suponha que a lista digitada seja: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8]. 
Para esta lista, o programa deve gerar as seguintes listas:
[4, 8, 8]
[1, 7, 9, 5, 3, 7, 9]

'''

lista = []
lista_par = []
lista_impar = []

for i in range(10):
    a = int(input("Digite um número: "))
    lista.append(a)

for e in lista:
    if e % 2 == 0:
        lista_par.append(e)
    else:
        lista_impar.append(e)
print("Lista", lista_par)
print("lista", lista_impar)



'''
3) Preencha duas tuplas com 5 números cada, informados pelo usuário. Concatene as duas tuplas e exiba a tupla resultante.
Dica: primeiro crie duas listas, e então, converta as listas em tuplas utilizando a função tuple.
tupla = tuple(lista)		# converte a lista em uma tupla

Exemplo: Suponha que as tuplas contenham os números:
(3, 1, 5, 3, 5)
(5, 5, 7, 3, 1).
Como resultado, o programa deve gerar a tupla:
(3, 1, 5, 3, 5, 5, 5, 7, 3, 1).
'''

lista1 = []
lista2 = []

for i in range(5):
    x = int(input("Digite um número para forma uma lista: "))
    lista1.append(x)
    tupla = tuple(lista1)
print(tupla)
for item in range(5):
    z = int(input("Digite um número para forma a segunda lista: "))
    lista2.append(z)
    tupla2 = tuple(lista2)
print(tupla2)

tupla_soma = tupla + tupla2
print(tupla_soma)


'''
4) Escreva uma função chamada intercala_numeros que recebe como entrada duas listas de três elementos e retorna uma lista de seis elementos, com os números intercalados.

Exemplo: Suponha que as listas de entrada da função sejam: 
[1, 2, 3]
[4, 5, 6] 
Para estas listas, a função deve retornar:
[1, 4, 2, 5, 3, 6]

'''

def intercala_numeros(lista3, lista4):
    intercalada = []
    for a, b in zip(lista3, lista4):
        intercalada.append(a)
        intercalada.append(b)        #zip ele é mais fácil pois ele entra nas duas listas.  
    return intercalada

lista3 = [1,2,3]
lista4 = [4,5,6]

listaintercalada = intercala_numeros(lista3, lista4)

for i in listaintercalada:
    print(i)





