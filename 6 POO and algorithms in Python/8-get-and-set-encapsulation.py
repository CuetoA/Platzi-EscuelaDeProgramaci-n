class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None
        
    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
            print(f'Region {region} correctly set')
        else:
            print(f'The {region} region is not allowed\n')
            
###### Programm

print('Starting code')
casilla = CasillaDeVotacion(123, ['CDMX', 'MORELOS'])
print(casilla.region)
casilla.region = "Michoacan"
casilla.region = "CDMX"