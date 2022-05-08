'''
1 
'''

arquivo = open('arquivo.txt', 'w', encoding='UTF-8')

for i in range(10):
    numero = int(input("Número: "))
    arquivo.write(str(numero) + '\n')

arquivo.close()



'''
2
'''

arquivo = open('arquivo.txt', 'r', encoding='UTF-8')

soma = 0

for linha in arquivo:
    soma += int(linha)
print(f"Valor da soma: {soma}")

arquivo.close()


'''
3
'''

arquivo = open('Par.txt', 'w', encoding='UTF-8')

for i in range(3):
    par = int(input("Digite um número par: "))
    arquivo.write((str)(par)+ '\n')

arquivo.close()


arquivo = open('Impar.txt', 'w', encoding='UTF-8')

for i in range(3):
    impar = int(input("Digite um número impar: "))
    arquivo.write((str)(impar) + '\n')

arquivo.close()


arquivo = open('Par.txt', 'r')

lista = []

for linha in arquivo:
    lista.append(int(linha))
    lista.sort()
print(lista)


arquivo = open('Impar.txt', 'r')

for linha in arquivo:
    lista.append(int(linha))
    lista.sort()
print(lista)


arquivo = open('Novo.txt' , 'w', encoding = 'UTF-8')

for x in lista:
    arquivo.write(str(lista) + '\n')

arquivo.close()


'''
4
'''
'''
ips = open('ips.txt', 'r')

validos = open('ips validos.txt', 'w')
invalidos = open('ips invalidos.txt', 'w')

for n in ips:
    lista = n.split('.')

    n1 = int(lista[0])
    n2 = int(lista[1])
    n3 = int(lista[2])
    n4 = int(lista[3])


    if n1 >= 1 and n1 <= 255 and \
       n2 >= 0 and n2 <= 255 and \
       n3 >= 0 and n3 <= 255 and \
       n4 >= 0 and n4 <= 255:
        validos.write(n)
    else:
        invalidos.write(n)

ips.close()
validos.close()
invalidos.close()
'''