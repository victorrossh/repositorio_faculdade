def maximo (a,b):
  
    if a>b:
        return("O primeiro valor é maior")
    elif a <b:
        return("O segundo valor é maior.")
    else:
        return("Os valores são iguais.")

n1 = int(input("Informe um valor: "))
n2=int(input("Informe um valor: "))

print(maximo (n1,n2))
