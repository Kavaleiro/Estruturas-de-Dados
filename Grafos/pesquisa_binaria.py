
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio -1 
        else:
            baixo = meio + 1
    return None

minha_lista = [1,2,3,4,5]
print(pesquisa_binaria(minha_lista, 5))