minutos = int(input("Quantos minutos foi utilizado ? "))

if minutos < 200:
    preço = 0.20

else:
    if minutos < 400:
        preço = 0.18

    else:
        preço = 0.15

custo = minutos * preço

print (f"Você vai pagar esse mês: R${custo}")   