from msilib.schema import Class


class Lavadora:
    
    def __init__(self) -> None:
        pass    
    
    def lavar(self, temperatura="caliente"):
        self._llenarTanque(temperatura)     # Using private method
        self._añadirJabon()
        self._lavar()
        self._centrifugar()
        
    def _llenarTanque(self, temperatura):
        print("Llenando el tanque")
        
    def _añadirJabon(self):
        print("Añadiendo jabón")
        
    def _lavar(self):
        print("Añadiendo jabón")
        
    def _centrifugar(self):
        print("Centrifugando")


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()