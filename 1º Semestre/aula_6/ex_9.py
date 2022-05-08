x = int(input("Digite o tamanho do primeiro arquivo: "))
y = int(input("Digite o tamanho do segundo arquivo: "))


if x > y:
    print("O primeiro arquivo é maior do que o segundo.")

elif x < y:
    print("O segundo é maior do que o primeiro arquivo.")   

else:
    print("O arquivos possuem o mesmo tamanho.")