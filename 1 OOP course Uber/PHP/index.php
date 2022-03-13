<?php

require_once('car.php');
require_once("UberX.php");
require_once("UberVan.php");
require_once("UberPool.php");
require_once("account.php");

$uberX = new UberX("YMT777", new Account("Scarlette Bello Barrón", "INE"), "Chevrolette", "Spark");
$uberX->printData();


$uberPool = new UberPool("MGE5707", new Account("Andrés Cueto", "INE"), "Suzuki", "Swift");
$uberPool->setPassenger(4);
$uberPool->printData();

$uberVan = new UberVan("ADA335", new Account("Ceres Hada", "34"), "hello2", "hello3");
$uberVan->setPassenger(6);
$uberVan->printData();
?>
