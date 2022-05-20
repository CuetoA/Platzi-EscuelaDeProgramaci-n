class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia

    def convertir_a_kilometros(self):
     return (self.distancia * 1.609344)
 
    # Método getter
    def obtener_distancia(self):
        return self._distancia

	# Método setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        self._distancia = valor
        
    # Función para eliminar el atributo _distancia
    def eliminar_distancia(self):
        del self._distancia

    distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)
 
avion = Millas()
avion.distancia = 200
print(avion.distancia)
print(avion.convertir_a_kilometros())