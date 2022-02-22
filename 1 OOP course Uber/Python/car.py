class Car:
    id = int
    license =str
    driver = str
    passenger = int
    
    def dataCar(self):
        print("License: ", self.license )
        print("Driver: ", self.driver )
        print("Passenger: ", self.passenger )