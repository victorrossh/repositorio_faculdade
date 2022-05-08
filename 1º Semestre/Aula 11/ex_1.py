valor = 0
soma = 0

while True:
    valor_produto = float(input("Digite o valor do produto: "))
    soma += valor_produto 
    valor += valor_produto
    x = input("Deseja comprar mais produtos (S ou N)? ")
     
    if x == "N":
        print(f"O valor da compra é de {soma:.2f}")
        caixa = input("Deseja fechar o caixa [S/N] ?")
        soma =0

        if caixa == "S":
            print(f"O lucro do caixa no dia foi de {valor:.2f}.")
            break


