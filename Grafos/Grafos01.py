import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

#Cria um grafo vzio
G = nx.Graph()

#adicionando vértices
G.add_node("v1")
G.add_node("v2")
G.add_node("v3")
G.add_node("v4")
G.add_node("v5")
print()
#Adiciona arestas
G.add_edge("v1", "v2")
G.add_edge("v2", "v3")
G.add_edge("v3", "v4")
G.add_edge("v4", "v5")
G.add_edge("v5", "v1")
G.add_edge("v2", "v4")
print()
#Lista dos vértices
print("Lista dos véttices")
print(G.nodes())
input()
print()
#Percorre o conjunto de vértices 
print("Percorrendo os vértices")
for v in G.nodes():
    print(v)
input()
print()

#Lista de Arestas 
print("Lista de arestas")
print(G.edges())
input()
print()

#Percorrendo as Arestas
print("Percorrendo as Arestas")
for a in G.edges():
    print(a)
input()
print()

#Mosta a lista de graus
print("Lista de graus de G")
print(G.degree())
input()
print()

#Acessa o gfrau do vértice v2 
print(f"O grau do vértice v2 é {G.degree()['v2']}")
input()
print()

#Grafo como lista de adjacências
print("Grafo como lista de adjacências")
print(G["v1"])
print(G["v2"])
print(G["v3"])
print(G["v4"])
print(G["v5"])
print()

#Obtém a matriz de adjacências do grafo G
print("Matriz de adjacências de G")
Adj = nx.adjacency_matrix(G)#retorna a matriz esparsa
print(Adj.todense())#Converte para matriz densa(padrão)
input()
print()

#Adiciona um campo peso em cada aresta do grafo 
G["v1"]["v2"]["peso"] = 5
G["v2"]["v3"]["peso"] = 10
G["v3"]["v4"]["peso"] = 2
G["v4"]["v5"]["peso"] = 7
G["v5"]["v1"]["peso"] = 4
G["v4"]["v2"]["peso"] = 8
input()
print()

#Lista cada aresta e seus respectivos pesos 
print("Adicionando pesos  as arestas")
for edge in G.edges():
    u = edge[0]
    v = edge[1]
    print("O peso da aresta ", edge, "vale", G[u][v]['peso'])
input()
print()

print("Plotando o grafo com imagem")
plt.figure(2)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()