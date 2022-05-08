produto = input("Produto desejado: ")
quantidade_adquirida = int(input("Digite a quantidade comprada: "))
preco_unitario = float(input("Digite o preço do produto comprado: "))

total = (quantidade_adquirida*preco_unitario)

if quantidade_adquirida <=5:
    desconto = preco_unitario*2/100
    valor_total = total - desconto
    print(f"O valor pago do produto é de R${valor_total:.2f}.")

elif quantidade_adquirida >5 and quantidade_adquirida <=10:
    desconto2 = preco_unitario*3/100
    valor_total2 = total - desconto2
    print(f"O valor pago do produto é de R${valor_total2:.2f}.")

else:
    desconto3 = preco_unitario*5/100
    valor_total3 = total - desconto3
    print(f"O valor pago do produto é de R${valor_total3:.2f}. ")
    
