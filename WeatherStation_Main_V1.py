""" 
File Name: WeatherStation_Main_V1.py
Author: Joe Lucas (JL4250)
Date Created: 26/11/2024
Last Modified: 
Description: This code uses classes created for four different sensors to read and display the readings of temperature, pressure, humidity and ambient light sensors.
"""

# Import Required Modules and Classes
import WeatherStation_HumiditySensor_v1 as humidity
import WeatherStation_LightSensor_V1 as LS
import WeatherStation_PressureSensor_v1 as pressure
import WeatherStation_TempSensor_V1 as temp
import machine

# Initiate I2C Communication Protocol
I2CPins = (machine.pin(5), machine.pin(4))
I2CObject = machine.I2C(0, I2CPins[0], I2CPins[1])

# Create Instances of Sensors
LSObject = LS.LightSensor(I2CObject)
sensors = LSObject

# Check Status of All Sensors
sensorStatusCheck = 0
for i in sensors:
    sensorStatusCheck += i.StatusCheck()

# Main Loop
