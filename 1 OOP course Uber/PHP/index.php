<?php

require_once('Car.php');
require_once('Account.php');

$car = new Car("AGM231", new Account("Oso" , "INE") );
$car->printData();