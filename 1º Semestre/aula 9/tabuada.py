valor = int(input("Digite a tabuada desejada: "))
i=0
if valor >=0 and valor<=9:
    while i <10:
        i+=1
        t = i*valor       
        print()
tabuada = 1

while tabuada <=10:
    numero= 1
    while numero <= 10:
        resultado = numero * tabuada
        print(f"{tabuada} x {numero} = {resultado}")
        numero +=1
    tabuada +=1