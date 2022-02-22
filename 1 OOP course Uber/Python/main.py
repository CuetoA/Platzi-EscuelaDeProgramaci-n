from car import Car

if __name__ == "__main__":
    print("Hola mundo")
    
    
    car = Car()
    car.license = "MGE277"
    car.driver = "Andrés Cueto"
    car.passenger = 5
    print( vars(car) )
    
    car2 = Car()
    car2.license = "NPR069"
    car2.driver = "Alejandor Velez"
    car2.passenger = 5
    car2.dataCar()