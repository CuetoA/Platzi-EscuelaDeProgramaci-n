<?php

require_once('car.php');
require_once("UberX.php");
require_once("UberPool.php");
require_once("account.php");

$uberX = new UberX("YMT777", new Account("Scarlette Bello Barrón", "INE"), "Chevrolette", "Spark");
$uberX->printData();


$uberPool = new UberPool("MGE5707", new Account("Andrés Cueto", "INE"), "Suzuki", "Swift");
$uberPool->printData();
?>