''' Exemplo
cadastro ={}

for i in range(2):
    cpf = int(input("CPF: "))
    nome = input("Nome: ")
    cadastro[cpf] = nome
print(cadastro)
'''


'''
Exercício 01

Preencha um dicionário com as informações de 5 produtos.
Utilize o nome do produto como chave e o preço como valor. 
Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00

Exemplo:
Veja um exemplo da estrutura do dicionário.
{'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0, 'Lápis': 1.50}

'''

catalogo = {}

for i in range(5):
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    catalogo[nome] = preco
print(catalogo)

for nome in catalogo:
    if catalogo [nome]>50:
        print(nome)

'''
Exercício 2 
Preencha um dicionário com os dados de 5 alunos.
Utilize o ra do aluno como chave e uma lista de três notas como valor.
Solicite os dados ao usuário.
Percorra o dicionário e exiba a média de cada aluno.

Exemplo:
Veja um exemplo da estrutura do dicionário.
{1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}

'''

cadastro = {}

for i in range(1):
    ra = int(input("RA: "))
    nota1 = float(input("Nota: "))
    nota2 = float(input("Nota: "))
    nota3 = float(input("Nota:"))
    lista = [nota1,nota2,nota3]
    cadastro[ra] = lista
print(cadastro)

for x in cadastro:
    lista = cadastro[ra]
    media = sum(lista)/len(lista)
    print(f"{media:.2f}")



'''
Exercício 03

Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade de vezes que essa vogal aparece no texto. 
A função deve receber o texto como entrada, e retornar o dicionário.

Exemplo:
Para o texto abaixo:
texto = 'faculdade de tecnologia impacta'
		

A função deve retornar o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o': 2, 'i': 2}

'''

def contaVogais(texto):
    vogais = {"a":0, "e":0, "i":0, "o":0, "u":0}

    for x in texto:
        if x in vogais:
            vogais[x] +=1

    return(vogais)
    
print(contaVogais('faculdade de tecnologia impacta'))




