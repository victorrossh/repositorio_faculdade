x = int(input("Digite um valor: "))
y =  int(input("Digite um valor: "))

if (x > y):
    y = x*y

    print(f"O valor de x maior que y recebe o valor de {y}")

elif (x < y): 
    x = x + y

    print(f"O valor da soma de x e y é de {x}")

else:
    y = x - y

    print(f"O valor de y é de {y}")