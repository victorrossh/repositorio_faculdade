base = float(input("Digite a área: "))
altura = float(input("Digite a altura: "))

if base <0:
    print("Não pode usar números que menor que 0.")

elif altura <0:
    print("Não pode usar números que menor que 0.")

else:
    area = 0.5*base*altura
    print(f"A área do triângulo é de {area}")

