
infinito =  float("inf")
grafo = {
    'd': {'a': 2, 'b': 4},
    'a': {'d': 2, 'c': 1, 'b': 3},
    'b': {'a': 3, 'd': 4, 'e': 2},
    'c': {'a': 1, 'f': 4},
    'e': {'b': 2, 'f': 3},
    'f': {'c': 4, 'e': 3}
}

grafo['a'] = {}
grafo['a']['d'] = 2
grafo['a']['c'] = 1
grafo['a']['b'] = 3

grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['d'] = 4
grafo['b']['e'] = 2

grafo['c'] = {}
grafo['c']['a'] = 1
grafo['c']['f'] = 4

grafo['e'] = {}
grafo['e']['b'] = 2
grafo['e']['f'] = 3

grafo['f'] = {}
grafo['f']['c'] = 4
grafo['f']['e'] = 3

custo = {}
custo['a'] = 2
custo['b'] = 4
custo['d'] = 0 #ponto de partida

pais = {}
pais['a'] = 'd'
pais['b'] = 'd'
pais['d'] = None

processados = []

def custo_mais_baixo(x):
    custo_baixo = float("inf")
    nodo_mais_baixo = None
    for nodo in x:
        C = x[nodo]
        if C < custo_baixo and nodo not in processados:
            custo_baixo = C
            nodo_mais_baixo = nodo
    return nodo_mais_baixo

    
nodo = custo_mais_baixo(custo)
while nodo is not None:
    C = custo[nodo]
    vizinho = grafo[nodo]
    for n in vizinho.keys():
        novo_custo = C + vizinho[n]
        if n not in custo:
            custo[n] = infinito
        if custo[n] > novo_custo:
            custo[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = custo_mais_baixo(custo)

def rota(pai, destino):
    rota = []
    atual = destino
    while atual is not None:
        rota.insert(0, atual)#inserindo nó atual no início da rota
        atual = pai.get(atual)# move para o nó pai
    return rota

print("ROTA PERCORRIDA")
for n in grafo.keys():
    if n != 'd':
        rot = rota(pais, n)
        print(f"{n} => {rot}")
print()
print("Custo final: ", custo)
print("Pais: ", pais)


