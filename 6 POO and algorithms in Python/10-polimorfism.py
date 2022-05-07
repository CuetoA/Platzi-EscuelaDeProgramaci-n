class Person:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def avanzar(self):
        print(f'I, {self.nombre}, am walking')
    
    
        
class Cyclist(Person):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def avanzar(self):
        print(f'I, {self.nombre}, am riding')
        

scar = Person('Scarlette')
andy = Cyclist('Andrés')

scar.avanzar()
andy.avanzar()