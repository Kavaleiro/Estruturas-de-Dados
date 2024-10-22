def quicksort(arr):
    if len(arr) < 2:
        return arr #Base
    else:
        pivo = arr[0] # caso recursivo
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([1,2,3,4,5,6]))