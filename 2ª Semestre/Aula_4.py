# 1

try:

    x = int(input("Primeiro valor: "))
    y = int(input("Segundo valor: "))
    z = x / y
    print('O resultado da divisão é: ', z)
except ZeroDivisionError:
    print("Divisão por zero.")
except ValueError:
    print("O valor informado não é considerado inteiro.")
except Exception:
    print("Erro inesperado.")
finally:
    print("Operação concluída com sucesso.")

# 2


def funcao_1():
    try:
        print('Início da função')
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(15):
            print(lista[i])
    except IndexError:
        print("Índice inexistente.")
print('Início do programa')
funcao_1()
print('Fim do programa')


# 3 

def buscar(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print("Indice não encontrado")

lista = []

for i in range(5):
    nome = input("Digite um nome: ")
    lista.append(nome)

print(buscar(lista, 8))

# 4

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
        print("Não é permitido RA inferior a 7 digitos.")
    except TypeError:
        print("O RA já está cadastrado")
print(alunos)




# 5


def converte_para_celsius(fahrenheit):
    celsius = (5.0/9.0) * (fahrenheit - 32)
    return celsius


def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit