import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f"{os.linesep}{nome} sim vale muito a pena pelas oportunidades de crescimento e bons salários e umas das linguagens que mais cresce no mundo.")
    elif resposta == '2':
        print (f"{os.linesep}{nome} isso varia muito do seu esforço e dedicação com a linguagem, tudo depende de quanto você sabe, não possui um tempo exato. ")
    elif resposta == '3':
        print (f"{os.linesep}{nome} a linguagem python você pode estudar através de cursos onlines no youtube ou pela Udemy. Mas as grandes universidades estão para os estudantes.")
    else:
        print("Digite apenas 1,2 ou 3")

def start():
    #Apresentar o chatboot
    print("Olá! Bom dia, vamos tirar algumas dúvidas sobre a linguagem python.")
    nome = input("Digite seu nome: ")
    email = input("Email: ")
    while True:
        resposta = input(f"O que você gostaria de saber {os.linesep} [1] - Vale a pena trabalhar com python ? {os.linesep} [2] - É complicado arrumar emprego com a linguagem Python ? {os.linesep} [3] - Onde eu posso estudar python ? ")
        sair = input("Deseja sair do chat [S/N] ? ").upper()
        if sair == "S":
            break
        processar_resposta(resposta, nome)


if __name__ == "__main__":
    start()