#OPERAÇÃO = + ; - ; * ; / 

var1 = float(input("Digite um número: "))
var2 = float(input("Digite outro número: "))
operaçao = input("Operação: ")

if (var1,var2):
    print(var1 , var2)

if operaçao == "+":
    soma = var1 + var2
    print (soma)

elif operaçao == "-":
    subtrair = var1 - var2
    print (subtrair)
   
elif operaçao == "*":
    multiplicar = var1 * var2
    print(multiplicar)
    
else:
    dividir = var1 / var2
    print(dividir)

