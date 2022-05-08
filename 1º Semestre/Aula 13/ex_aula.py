listaNotas=[]
for i in range(10):
  valorDigitado=float(input("Digite o %d° nota: "%(i+1)))
  listaNotas.append(valorDigitado)

soma=sum(listaNotas)
tam = len(listaNotas)
media = soma/tam
print("A nota média é", media)
menor = min(listaNotas)
print("A menor nota foi", menor)
maior = max(listaNotas)
print("A maior nota foi", maior)
listaNotas.sort()
print("Lista em ordem crescente", listaNotas)