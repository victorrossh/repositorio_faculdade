n = int(input("Digite quantas pessoas serão registradas: "))
soma = 0
x = 0
while x < n:
    idade = int(input("Digite a idade da %d° pessoa: " %x))
    soma = soma + idade #acumulador
    x = x + 1 #incrimento - soma 1 ao valor que estou testanto no loop.

media = soma/n
print(f"Média de idade das pessoas: {media}")

if media >= 0 and media <= 25:
    print("A turma é jovem.")
elif media >= 26 and media <= 60:
    print("A turma é adulta.")
elif media > 60:
    print("A turma é idosa.")