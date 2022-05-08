lista = []
count = 10

for i in range(10):
    nome = lista.append(input("Digite um nome: "))

inserir_dados = input("Digite mais um: ")

for x in lista:
    if x == inserir_dados:
        print("Achei")
        break
else:
    print("Não achei")