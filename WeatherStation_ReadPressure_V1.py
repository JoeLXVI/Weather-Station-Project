""" 
File Name: WeatherStation_ReadPressure_V1.py
Author: Sam Young (SY947) 
Date Created: 26/11/2024
Last Modified: 
Description: This code defines a class for a pressure sensor including attributes and methods to allow for the reading and display of sensor data.
"""
# Import Required Modules
import time
import machine
import WeatherStation_PressureSensor_v1 as PS

I2C = machine.I2C(0,machine.pin(5),machine.pin(4))
PSobject = PS.PressureSensor(I2C)

while PSobject.StatusCheck():
    time.sleep(1)
    pressure_data = PSobject.ReadData()
    print(pressure_data)