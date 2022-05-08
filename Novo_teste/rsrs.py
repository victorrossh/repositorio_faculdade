def pertence(lista,item1,item2):
    if item1 and lista and item2 and lista:
        return True
    else:
        return False

def substituir (lista,novo,velho):
    lista = []
    
    for x in range(len(lista)):
        if lista[x]==novo:
            lista[x]==velho
            lista.append(x)
    return lista

def posicoes (tupla,item):
    lista=[]

    for x in range(len(tupla)):
        if item == tupla[x]:
            lista.append(x)
    return lista

def reprovados (alunos,nome):
    lista = []

    for x in alunos:
        listanotas = alunos[x]
        resultado = sum(listanotas)/len(alunos[x])
        if resultado <=6:
            lista.append(x)
    return lista


def excluir_nota (alunos,nome):
    dic = {}
    for x in alunos:
        if x in nome:
            alunos[nome].pop(0)
    return dic


def menor_nota(alunos):
    dic = {}

    for x in alunos:
        Menornota = min(alunos[x])
        dic[x] = Menornota
    return dic



