"""def busca_menor(arr):
    menor = arr[0]
    menor_ind = 0
    for i in range (1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_ind = i
    return menor_ind
def ordenar(arr):
    novoArr = []
    for i in range (len(arr)):
        menor = busca_menor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenar([5, 3, 6, 2, 10]))
"""
#Listas Encadeadas 
inicio = {}
anterior = {}
proximo = {}
chave = {}

def list_search(l,k):
    x = inicio.get(l)
    while x is not None and chave[x] !=k:
        x = proximo[x]
    return x

def list_insert(l, k):
    chave[k] = k
    proximo[k] = inicio.get(l)
    if inicio.get(l) is not None:
        anterior[inicio[l]] = k
    inicio[l] = k
    anterior[k] = None

def list_delete(l,k):
    x = list_search(l, k)
    if x is None:
        return
    if anterior[x] is not None:
        proximo[anterior[x]] = proximo[x]
    else: 
        inicio[l] = proximo[x]
    if proximo[x] is not None:
        anterior[proximo[x]] = anterior[x]

list_insert('L', 1)
list_insert('L', 4)
list_insert('L', 16)
list_insert('L', 9)
list_insert('L', 25)
print("Inserções da lista encadeada")
x = inicio['L']
while x is not None:
    print(f"No: {chave[x]}")
    x = proximo[x]
print()
print("Deletando da lista encadeada")
list_delete('L', 4)
x = inicio['L']
while x is not None:
    print(f"No: {chave[x]}")
    x = proximo[x]

print()
print("Procurando na lista Encadeada")
print()
n  = 16
if list_search('L', n) is not None:
    print(f" No: {list_search('L', n)}")
else:
    print("O que você procura não está aqui...")