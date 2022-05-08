l1 = float(input("Digite o valor do primeiro lado: "))
l2 = float(input("Digite o valor do segundo lado: "))
l3 = float(input("Digite o valor do terceiro lado: ")) 

if l3 < (l3+l2) or l2 < (l1+l3) or l3 < (l1+l2):
    print("Pode ser um triângulo " ,end='')

    if l1 == l2 == l3:
        print("Equilátero")
    
    elif l1!=l2!=l3:
        print("Escaleno")
    else:
        print("Isósceles")

else:
    print("Não pode dar triângulo.")





        
