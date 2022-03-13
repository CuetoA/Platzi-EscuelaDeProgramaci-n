from car     import Car
from account import Account
from uberBlack import UberBlack

if __name__ == "__main__":
    print("Hola mundo")
    
    
    car = Car("MGE277",  Account("Andrés Cueto" , "Visa") )
    car.dataCar()
    
    car2 = Car("NPR069", Account("Alejandro Velez" , "INE") )
    car2.dataCar()
    
    car3 = UberBlack("NPM5576", Account("Scarlette Bello", "kjno"), ["hola"], ["adios"] )
    car3.dataCar()
