try:
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z = x / y
    print('O resultado da divisão é:', z)
except ZeroDivisionError:
    print("Divisão por zero não existe")
except ValueError:
    print("Somente números inteiros")
except Exception:
    print("Erro inesperado")
finally:
    print("Fim do programa")

def funcao_1():
    try:
        print('Início da função')
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(15):
            print(lista[i])
    except IndexError:
        print("Índice inexistente.")
        print('Fim da função')
    
print('Início do programa')
funcao_1()
print('Fim do programa')


def buscar(lista,indice):
    try:
        return lista[indice]
    except IndexError:
        print("Índice incorreto")



lista = []
for i in range(5):
    nome = str(input("Nome: "))
    lista.append(nome)

print(buscar(lista, 8))


alunos = {}

for i in range(5):
    try:
        ra = int(input('RA: '))
        if len(str(ra)) != 7:
            raise ValueError
        if ra in alunos:
            raise TypeError 
        nome = input('Nome: ')
        alunos[ra] = nome
    except ValueError:
        print("RA não possui 7 digítos")
    except TypeError:
        print("RA existente")
print(alunos)

