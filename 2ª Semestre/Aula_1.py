'''
EXERCÍCIO 1:
Implemente a função 'soma' que recebe dois números e retorna o resultado
da soma desses dois números.
Lembre-se que a função deve utilizar a instrução return, para devolver
o resultado.
'''
# def não precisa de entrada de valores.

def somar (a,b):
    return a+b
print(somar(3, 10))

'''
EXERCÍCIO 2:
Implemente a função 'quadrado' que recebe um número e retorna o resultado
desse número ao quadrado.
'''

def quadrado(a):
    return a**2
print(quadrado(5))

'''
EXERCÍCIO 3:
Implemente a função 'soma_dos_quadrados' que receba dois numeros e devolve
a soma dos seus quadrados.
Você pode utilizar a função 'quadrado' definida anteriormente para
facilitar a implementação.
'''

def soma_dos_quadrados(a,b):
    return quadrado(a) + quadrado(b)
print(soma_dos_quadrados(3, 5))


'''
EXERCÍCIO 4:
Implemente a função 'media', que recebe três valores numéricos e retorna
a média aritmética dos valores.
'''

def media(a,b,c):
    d = (a+b+c)/3
    return d
print(media(10, 8, 9))


'''
EXERCÍCIO 5:
Implemente a função 'calcular_salario', que recebe o salário atual de um
funcionário e retorna o salário com um reajuste de aumento, sendo que:
- Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
- Caso contrário, o funcionário receberá 15% de aumento.
'''

def calcular_salario(salario):
    if salario > 2000:
        salario += (salario *7)/100
    else:
        salario += (salario *15)/100
    return salario
print(calcular_salario(1000))
print(calcular_salario(3000))    

'''
EXERCÍCIO 6:
Implemente a função 'soma_divisores', que recebe como parâmetro de entrada
um número positivo e retorna a soma de todos os divisores desse número.
Por exemplo:
- caso o número seja 15, o retorno deve ser 24 (1 + 3 + 5 + 15).
- caso o número seja 30, o retorno deve ser 72 (1 + 2 + 3 + 5 + 6 + 10 + 15 + 30)
'''

def soma_divisores(n):
    a = 1
    soma = 0
    while a <=n:
        if n%a ==0:
            soma = soma + a

        a+=1 
    return soma
print(soma_divisores(30))


'''
EXERCÍCIO 7:
Implemente a função 'fatorial' que recebe um número positivo e retorna o fatorial desse número.
O fatorial de um número N é o produto dos números naturais consecutivos de 1 até N.
Por exemplo:
- O fatorial de 5 é 120 (1 * 2 * 3 * 4 * 5)
- O fatorial de 10 é 3628800 (1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)
'''

def fatorial(n):
    fat = 1    # multiplicação de valores sempre 1 / se for soma é 0.
    a = 1      # a = [1,2,3,4.... n]
    while a <=n:
        fat = fat *a
        a+=1
    return fat
print(fatorial(5))


def fatorial_for(n):

    fat = 1
    for a in range(1, n+1):
        
        fat = fat*a
    return fat
print(fatorial_for(5))