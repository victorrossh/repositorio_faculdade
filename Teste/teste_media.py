contador = 0 
x = 0  

while contador < 10:
    nota1 = int(input("Digite o valor da nota: "))
    nota2 = int(input("Digite o valor da segunda nota: "))
    media = (nota1 + nota2)/2
    x +=1
    print(f"A sua media é de {media}")
    contador +=1
    