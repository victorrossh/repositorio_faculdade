'''
Cardápio:

Especificação
Código Preço

Cachorro Quente
100 R$ 10,50

Bauru Simples
101 R$ 10,00

Bauru com ovo
102 R$ 10,50

Hambúrguer
103 R$ 15,50

Cheeseburguer
104 R$ 17,50

Refrigerante
105 R$ 5,00
'''
preco = 0
while True:
    preco_produto = 0
    pedido = int(input("Digite o código do pedido: "))
    quantidade = int(input("Digite a quantidade desejada: "))

    if pedido == 100:
        preco_produto += 10.50
    elif pedido == 101:
        preco_produto += 10.00
    elif pedido == 102:
        preco_produto += 10.50
    elif pedido == 103:
        preco_produto += 15.50
    elif pedido == 104:
        preco_produto += 17.50
    else:
        preco_produto += 5.00
    
    preco_produto = preco_produto*quantidade
    preco += preco_produto

    x = input("Deseja encerrar com o pedido ? [sim/não]")

    if x == "sim":
        print(f"A conta do seu pedido foi de {preco:.2f}")
        break