x = 0
y = 0
soma_nota = 0


while x <2 : 
    while y <4:

        
        nota = float(input("Digite sua nota: "))
        soma_nota += nota
        y +=1
    media = soma_nota/2
    print(f"A média da turma é {media:.2f}")
    
    media = 0
    soma_nota = 0
    y = 0
    x+=1
       