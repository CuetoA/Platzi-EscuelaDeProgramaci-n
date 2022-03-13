class Main{

    public static void main(String[] args) {
        
        UberX car = new UberX("AMQ123", new Account("Andres Cueto", "AND123"), "Suzuki", "Swift");
        car.setPassenger(6);
        car.printDataCar();

        UberPool car2 = new UberPool("YMI270", new Account("Scarlette Bello", "SCR123"), "hello", "hello2");
        car2.setPassenger(6);
        car2.printDataCar();

        // UberVan car2 = new UberVan("YMI270", new Account("Scarlette Bello", "SCR123"), "hello", "hello2");
        // car2.setPassenger(6);
        // car2.printDataCar();
    }
}