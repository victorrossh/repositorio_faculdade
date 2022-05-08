nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = 6
nota_total = (nota1+nota2+nota3)/3


if nota_total > media:
    print("O aluno foi aprovado com a média %.2f"%nota_total)

else:
    print("O aluno foi reprovado com a média %.2f"%nota_total)
