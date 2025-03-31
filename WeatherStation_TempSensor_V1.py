""" 
File Name: WeatherStation_TempSensor_V1.py
Author: Cameron Jafry (CJ769)
Date Created: 26/11/2024
Last Modified: 
Description: This code defines a class for a temperature sensor including attributes and methods to allow for the reading and display of sensor data.
"""
import machine

class TemperatureSensor:
    def __init__(self, pin ):
        self.pin = machine.ADC(pin) #setup ADC pin
        self.reference_voltage = 3.3 #rp pico value

    def read_temperature(self):
        raw_value = self.pin.read_u16()
        voltage = (raw_value / 65535) * self.reference_voltage
        temperature_kelvin = voltage / 0.01
        temperature_celsius = temperature_kelvin - 273.15
        return temperature_celsius
    
    def status_check(self):
        data = self.pin.read_u16()
        if data > 0:
            print("LM335: Sensor responding") 
            return True
 
        else:
            print("LM335: Invalid sensor data")  

            return False      

    
