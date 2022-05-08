quant_max= int(input("Digite a quantidade máxima: "))
quant_min = int(input("Digite a quantidade mínima: "))
estoque = int(input("Digite a quantidade de estoque: "))

quantidade_media = (quant_max + quant_min)/2

if estoque >= quantidade_media:
    print("Não efetuar a compra dos produtos.")
else:
    print("Efetuar a compra dos produtos.")