
def mergeSort(lista):
    if len(lista) > 1:
        # Devide the list
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        mergeSort(izquierda)
        mergeSort(derecha)
        
        # Start sorting of small array
        i = 0
        j = 0
        k = 0
        
        # Partiali sort two arrays with remmanents
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        
        # Doesn't sort, but put arrays into place
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    
    return lista


if __name__ == "__main__":
    l = [5,4,2,1,3]
    ordenada = mergeSort(l)
    
    print(f'l: {l}')
    print(f'o: {ordenada}')