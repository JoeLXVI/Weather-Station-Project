""" 
File Name: WeatherStation_ReadHumidity_V1.py
Author: Mlles Perandin-Grainger (MPG54)
Date Created: 26/11/2024
Last Modified: 
Description: This code reads data from a WSEN_HIDS humidity sensor
"""
# Import Required Modules
import time
import machine
import WeatherStation_HumiditySensor_v1 as HS

# Innitialise I2C communication
I2C = machine.I2C(0, machine.pin(5), machine.pin(4))
HSObject = HS.HumiditySensor(I2C)
# Continuously read humidity sensor and print data
while HSObject.StatusCheck():
    time.sleep(1)
    HumidityData = HS.read_humidity()
    print(HumidityData)