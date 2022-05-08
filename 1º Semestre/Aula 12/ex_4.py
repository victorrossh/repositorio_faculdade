x = 0
par = 0
impar = 0
while x <2:
    numero = int(input("Digite um número: "))

    if numero%2==0:
        par +=1
    else:
        impar +=1

    x+=1    
print(f"A quantidade de números pares é de {par}")
print(f"A quantidade de números ímpares é de {impar}")
