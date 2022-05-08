eleitores = int(input("Digite o números de eleitores: "))
brancos = int(input("Digite o valor de votos brancos: "))
nulos = int(input("Digite o valor de votos nulos: "))
validos = int(input("Digite o valor de votos válidos: "))

conta_branco = (brancos/eleitores)*100
conta_nulo = (nulos/eleitores)*100
conta_valido = (validos/eleitores)*100

print(f"O número de votos brancos é de {conta_branco:2f} e votos nulos é de {conta_nulo:2f},votos válidos é de {conta_valido:2f}.")

