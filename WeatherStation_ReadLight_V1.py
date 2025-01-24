"""
File Name: WeatherStation_ReadLight_V1.py
Author: Robbie Votta (RV434)
Date Created: 22/01/2025
Last Modified:  22/01/2025
Description: This code reads data from a VEML6031 sensor using the machine library and a created class
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
