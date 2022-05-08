lata = int(input("Digite a quantidade de latas: "))
garrafa6 = int(input("Digite a quantidade de garrafas de 600 ML: "))
garrafa2 = int(input("Digite a quantidade de garrafas de 2 litros: "))

lata = 0.35*lata
garrafa6 = 0.6*garrafa6
garrafa2 = 2*garrafa2

total_litros = lata + garrafa6 + garrafa2

print(f"Vcoê comprou {total_litros} litros.")


