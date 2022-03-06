class Main{

    public static void main(String[] args) {
        
        Car car = new Car("AMQ123", new Account("Andres Cueto", "AND123"));
        car.license = "AMQ123";
        car.printDataCar();

        Car car2 = new Car("YMI270", new Account("Scarlette Bello", "SCR123"));
        car2.printDataCar();
    }

}