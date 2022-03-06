from car     import Car
from account import Account

if __name__ == "__main__":
    print("Hola mundo")
    
    
    car = Car("MGE277",  Account("Andrés Cueto" , "Visa") )
    car.dataCar()
    
    car2 = Car("NPR069", Account("Alejandro Velez" , "INE") )
    car2.dataCar()