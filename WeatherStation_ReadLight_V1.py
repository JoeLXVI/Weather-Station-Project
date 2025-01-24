"""
File Name: WeatherStation_ReadLight_V1.py
Author: Robbie Votta (RV434)
Date Created: 22/01/2025
Last Modified:  22/01/2025
Description: This code defines a class for a light sensor including attributes and methods to allow for the reading and display of sensor data.
"""

import WeatherStation_LightSensor_V1 as LS


import machine
import time


I2C = machine.I2C(0, machine.pin(5), machine.pin(4))
LSObject = LS.LightSensor(I2C)
while LSObject.StatusCheck():
    time.sleep(1)
    LightData = LS.ReadData()
    print(LightData)
