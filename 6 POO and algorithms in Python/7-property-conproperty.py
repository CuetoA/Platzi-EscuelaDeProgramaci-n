class Millas:
    def __init__(self):
        self._distancia = 0

    def convertir_a_kilometros(self):
     return (self._distancia * 1.609344)
 
    # Método getter
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia

	# Método setter
    def definir_distancia(self, recorrido):
        print("Llamada al método setter")
        self._distancia = recorrido
        
    # Función para eliminar el atributo _distancia
    def eliminar_distancia(self):
        del self._distancia

    distanciaDistinta = property(obtener_distancia, definir_distancia, eliminar_distancia)
 
avion = Millas()
avion.distanciaDistinta = 200
print(avion.distanciaDistinta)