senha = int(input("Digite a senha: "))

while senha != 1234:
    senha = int(input("Digite a senha: "))
    if senha == 1234:
        break
print("Acesso permitido")
        
