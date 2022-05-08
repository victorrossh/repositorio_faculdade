x = float(input("Digite o preço do primeiro produto: "))
y = float(input("Digite o preço do segundo produto: "))
z = float(input("Digite o preço do terceiro produto: "))

if x < y and z > x: 
    print("O preço do primeiro produto é menor.")

elif y < x and z > y:
    print("O preço do segundo produto é menor")

elif z < x and y > z:
    print("O preço do terceiro produto é menor")

else:
    print("O 3 valores são iguais.")


