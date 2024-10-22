def buscar_menor(arr):
    menor = arr[0]#armazena o menor valor 
    menor_indice = 0#armazena o indice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):#ordenação de um array
    novoArr = []
    for i in range(len(arr)):
        menor = buscar_menor(arr)#encontra o menor Array
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([5,3,6,2,10]))