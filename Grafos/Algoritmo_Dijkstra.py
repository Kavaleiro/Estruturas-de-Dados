grafo = {}#criando um grafo
grafo["inicio"] = {}#criando um grafo

grafo["inicio"]["a"] = 6#adicionando peso neste grafo
grafo["inicio"]["b"] = 2
#print(grafo["inicio"].keys())#visualizando os valores desse grafo

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

#tabela hash para adicionar o custo de cada vértice
infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

#criando uma tabela pai
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

#pseudocódigo
"""
1 - Enquanto houver grafos a serem processados
2 - Pegue o vértice que está mais próximo
3 - Atualize os custos para os seus vizinhos
4 - Se qualquer um dos custos dos vizinhos forem atualizado, atualize também o pai
5 - Marque o vértice processado 
"""
def ache_no_custo_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:#Vá por cada vértice
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:#Se for o vértice de menor custo até o momento e ainda não tiver sido processado
            custo_mais_baixo = custo #atribua como o novo vértice de menor custo.
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_baixo(custos)#Encontrar o custo + baixo q ñ foi processado
while nodo is not None:
    custo_atual = custos[nodo]
    vizinhos = grafo[nodo]
    for i in vizinhos.keys():#percorre todos os vizinhos desse vértice
        novo_custo = custo_atual + vizinhos[i]
        if custos[i] > novo_custo:#Caso seja mais barato chegar a um vizinho a partir desse vértice
            custos[i] = novo_custo#atualiza o custo dele.
            pais[i] = nodo#Esse vértice se torna o novo pai para o vizinho
    processados.append(nodo)#Marca o vértice como processado
    nodo = ache_no_custo_baixo(custos)

print("Custos finais:", custos)
print("Pais:", pais)
