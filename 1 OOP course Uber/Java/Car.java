public class Car {
    Integer id;
    String license;
    Account driver;
    Integer passenger;


    public Car (String license, Account driver){
        this.license = license;
        this.driver = driver;
    }

    void printDataCar(){
        System.out.println("License: " + license);
        System.out.println("Driver: " + driver.name);
        System.out.println("Passenger: " + passenger);
        System.out.println();
    }
    
}