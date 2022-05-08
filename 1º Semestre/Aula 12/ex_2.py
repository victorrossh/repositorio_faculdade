x = 0
y = int(input("Digite a quantidade de números: "))
impar=0
par=0

while x < y:
    n = int(input("Digite um número: "))

    if n%2 ==0:
        par = par + n

    else:
        impar = impar + n

    impar += n
    par += n
    y+=1
    print(f"A soma dos números pares é {par}")
    print(f"A soma dos números ímpares é {impar}")