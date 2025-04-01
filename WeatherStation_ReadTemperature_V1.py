"""
File Name: WeatherStation_ReadTemperature_V1.py
Author: Joe Lucas (JL4250)
Date Created: 26/11/2024
Last Modified:
Description: This code reads and displays data freom a temperature sensor
"""

# Import required modules
import WeatherStation_TempSensor_V1 as TS
import machine
import time

TSObject = TS.TemperatureSensor(30)

# Read data in every second
while TSObject.status_check():
    time.sleep(1)
    data = TSObject.read_temperature()
    print(f"Temperature: {data}°C")
