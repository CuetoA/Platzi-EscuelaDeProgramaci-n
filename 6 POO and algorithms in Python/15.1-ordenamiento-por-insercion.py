# Insertion Sort

arreglo = [5,6,4,1]

for n in range(1, len(arreglo)): #
    posicion_actual = n
    valor_actual = arreglo[n]  
    
    while posicion_actual > 0 and valor_actual < arreglo[posicion_actual - 1]:
        arreglo[posicion_actual] = arreglo[posicion_actual - 1]
        posicion_actual -= 1
        
    arreglo[posicion_actual] = valor_actual
    
print(arreglo)