produto = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a percentual de desconto: "))

valor_desconto = (produto * desconto)/100

preço = produto - valor_desconto
print (valor_desconto)
print ("O preço pago será %.2f"%preço)            