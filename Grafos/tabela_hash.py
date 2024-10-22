primos = {
    "a": 2,
    "b": 3,
    "c": 5,
    "d": 7,
    "e": 11,
    "f": 13,
    "g": 17,
    "h": 19,
    "i": 23,
    "j": 29,
    "k": 31,
    "l": 37,
    "m": 41,
    "n": 43,
    "o": 47,
    "p": 53,
    "q": 59,
    "r": 61,
    "s": 67,
    "t": 71,
    "u": 73,
    "v": 79,
    "w": 83,
    "x": 89,
    "y": 97,
    "z": 101,
}

  
def soma(nome):
    soma = 0
    for char in nome:
        if char in primos:
            soma += primos[char]
        else:
            print("Esse não é uma letra válida")
    return soma


print(soma("bag"))

# tabela = {}
# tabela["a"] = []
# def juntos(nome):
#    if nome[0] == 'a':
#        tabela["a"].append(nome)
#    else:
#        print("próximo")
# juntos("felipe")
# juntos("aiane")
# juntos("ana")
# print(tabela)


# votaram = {}
# def verificar(nome):
#    if votaram.get(nome):
#        print("Ele já vtou")
#    else:
#        votaram[nome] = True
#        print("Pode votar!!")

# verificar("felipe")
# verificar("josé")
# verificar("felipe")

# EXEMPLO
# cache = {}
# def peg_pag(url):
# if cache.get(url):
#    return cache[url]
# else:
# dados = pegar_pagina_servidor(url)
# cache[url] = dados
# return dados
