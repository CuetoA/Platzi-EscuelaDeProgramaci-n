<?php
class Car {
    public $id;
    public $license;
    public $driver;
    public $passenger;

    public function __construct($license, $driver){
        $this->license = $license;
        $this->driver = $driver;
    }

    public function printData(){
        echo "License: {$this->license}\n
              Driver: {$this->driver->name}\n
              Document: {$this->driver->document}\n
              Passengers: {$this->passenger}\n
              
              ";
    }

    public function getPassenger(){
        return $this->$passenger;
    }

    public function setPassenger($passenger){
        if($passenger == 4){
            $this->$passenger = $passenger;
        }else{
            echo "Necesitas 4 pasajeros";
        }
    }
}