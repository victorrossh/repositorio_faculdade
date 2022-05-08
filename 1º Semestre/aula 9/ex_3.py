fim = int(input("Digite o valor final: "))
x = 0

while x < fim:
    x = x+1
    if x%2 == 0:
        print("Par",x)
    else:
        print("Ímpar",x)

