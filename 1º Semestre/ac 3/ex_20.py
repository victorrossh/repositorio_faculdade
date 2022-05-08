x = 0
soma = 0
mercadoria = int(input("Digite a quantidade de mercadoria em estoque: "))
while x <mercadoria:

    valor_mercadoria = float(input("Digite o valor da mercadoria: "))

    soma +=valor_mercadoria
    media = soma/mercadoria
    x+=1
print(F"A média de valor por mercadoria é {media}.")
print(f"O valor total em estoque é de {soma}.")