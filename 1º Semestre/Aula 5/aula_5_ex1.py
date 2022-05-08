velocidade = int(input("Digite sua velocidade: "))

if velocidade > 80:
    multa= (velocidade -80)*5
    print(f"O valor da multa será de {multa}")

else:
    print("Nenhum valor cobrado")

