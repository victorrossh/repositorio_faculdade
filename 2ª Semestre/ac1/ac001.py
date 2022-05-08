import teste_po

'''
1) Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada uma lista e dois itens e retorna True, se os dois itens estiverem armazenado na lista, e False, caso contrário.
'''


def pertence(lista, item1, item2):
    if item1 and lista and item2 and lista:
        return True
    else:
        return False

'''
2)Escreva uma função chamada 'substituir' que recebe como argumentos de entrada uma lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências do item velho são substituídas pelo item novo. 
'''


def substituir(lista, velho, novo):
    lista = []

    for x in range(len(lista)):
        if lista[x] == novo:
            lista[x] == velho
    return lista

'''
3) Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada uma tupla e um item, e retorna uma lista contendo todos os índices em que o item aparece na tupla. Caso o item nao exista na tupla, deve retornar uma lista vazia. 
'''


def posicoes(tupla, item):
    lista = []

    for x in range(len(tupla)):
        if item == tupla[x]:
            lista.append(x)
    return lista

'''
4) Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de notas. Escreva uma função chamada 'reprovados' que recebe como argumentos de entrada o dicionário e retorna uma lista com o nome dos alunos reprovados. Considere que o aluno é reprovado se a média das suas notas é inferior a 6. Caso nenhum aluno seja reprovado, deve retornar uma lista vazia. 
'''


def reprovados(alunos):
    lista = []

    for x in alunos:
        listanotas = alunos[x]
        resultado = sum(listanotas)/len(alunos[x])
        if resultado <= 6:
            lista.append(x)
    return lista


'''
5) Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos de entrada o dicionário e o nome de um aluno. A função deve excluir a primeira nota desse aluno e retornar o dicionário com as alterações realizadas. Se o aluno não existir no dicionário, deve retornar o dicionário sem alterações.

'''


def excluir_nota(alunos, nome):
    dic = {}

    for x in alunos:
        if x in nome:
            alunos.pop[nome] = 0
    return alunos

'''
6) Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de notas. Escreva uma função chamada menor_nota que recebe como argumentos de entrada o dicionário e retorna outro dicionário com o nome e a menor nota de cada aluno.

'''


def menor_nota(alunos):
    dic = {}

    for x in alunos:
        Menornota = min(alunos[x])
        dic[x] = Menornota
    return dic