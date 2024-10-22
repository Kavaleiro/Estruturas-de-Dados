#Criando um exemplo de grafo
grafo = {}
grafo["voce"] = ["alice", "bob", "claire"] #O grafo principal

grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["tom", "jony"]
#Esses a baixo não tem vizinhos
grafo["anuj"] = []
grafo["peggy"] = []
grafo["tom"] = []
grafo["jony"] = []

#Implementação em pseudo código 
"""
1 - crie um fila Contendo todas as pessoas que devem ser verificadas
2 - Retire uma pessoa da fila 
3 - Confira se esta pessoa é uma vendedora de manga
4 - se sim(Achou)
    se não(adicione todos os vizinhos dela na fila)
5 - Repita o processo
6 - Caso a fila esteja vazia. Não existem vendedores de manga
"""
# criando o código
from collections import deque

# funcçaõ para pessoa_e_vendedor
def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'
def pesquisa(nome):
    fila_de_pesquisa  = deque()#criando uma nova lista
    fila_de_pesquisa += grafo[nome]#colocando a minha lista
    verificados = []# para evitar loops
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()#Primeira pessoa da fila
        if pessoa not in verificados:
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de manga")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificados.append(pessoa)
    return False

pesquisa("voce")





