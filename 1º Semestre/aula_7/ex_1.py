nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))
media = (nota1+nota2+nota3)/3

if media >= 9.0:
    print ("A")
elif media >= 7.5 and media <9.0:
    print("B")

elif media >=6.0 and media < 7.5:
    print("C")

elif media >=4.0 and media <6.0:
    print("D")

else:
    print("E")


  