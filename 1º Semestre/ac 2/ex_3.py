maça = int(input("Digite a quantidade de maçã: "))

if maça < 12:
    total= maça*0.30
    print(f"O valor pago será de {total}")

else:
    total = maça*0.25
    print(f"O total pago será de {total}")