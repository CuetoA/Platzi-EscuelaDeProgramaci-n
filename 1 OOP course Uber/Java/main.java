class Main{

    public static void main(String[] args) {
        
        UberX car = new UberX("AMQ123", new Account("Andres Cueto", "AND123"), "Suzuki", "Swift");
        car.license = "AMQ123";
        car.setPassenger(6);
        car.printDataCar();

        // Car car2 = new Car("YMI270", new Account("Scarlette Bello", "SCR123"));
        // car2.printDataCar();
    }

}