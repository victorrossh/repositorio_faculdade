maior = 0
todos = 0
x = 0
while x <10:
    idade = int(input("Digite sua idade: "))

    if idade > maior: 
        maior = idade
       

    if idade >= 12 and idade <=18:
        todos+= 1
        
    x += 1
print(maior)
print (todos)



