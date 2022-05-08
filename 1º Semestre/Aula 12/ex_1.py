x = 0
y = float(input("Informe a quantidade de notas: "))
var1 =0
var2= 0
soma = 0
soma_nota = 0
while x < y:
    n = float(input("Informa as notas: "))
    
    if n > 0:
        var1 +=1
    
    else: 
        var2+=1    

    soma_nota += n
    soma +=1
    x+=1
    print(f"O valor da média aritmetica é de {soma_nota}")
    print(f"A quantida de notas positivas é de {var1}")
    print(f"A quantidade de notas negativas é de {var2}")

        

    
