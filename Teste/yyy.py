contador = 0
x = 0

while contador <10:
    nota1 = float(input("Digite sua nota:  "))
    nota2 = float(input("Digite sua nota: "))
    media = (nota1 + nota2)/2
    x+=1
    print(f"Sua média é de {media}")
    contador +=1