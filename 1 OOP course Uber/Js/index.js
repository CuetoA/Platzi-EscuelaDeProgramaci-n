var account = new Account("Andrés Cueto", "INE");
var car = new Car("AW324", account);
car.passenger =4;
car.printDataCar();

var car2 = new UberVan("AW324", new Account("Scarlette Bello Barrón", "INE"), "hola", "hola2");
car2.passenger = 5;
car2.printDataCar();