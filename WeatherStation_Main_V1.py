"""
File Name: WeatherStation_Main_V1.py
Author: Joe Lucas (JL4250)
Date Created: 26/11/2024
Last Modified: 17/03/2025
Description: This code uses classes created for four different sensors to read and display the readings of temperature, pressure, humidity and ambient light sensors.
"""

# Import Required Modules and Classes
import WeatherStation_HumiditySensor_v1 as HS
import WeatherStation_LightSensor_V1 as LS
import WeatherStation_PressureSensor_v1 as PS
import WeatherStation_TempSensor_V1 as TS
import machine
import time

# Initiate I2C Communication Protocol
I2CPins = (machine.Pin(5), machine.Pin(4))
I2CObject = machine.I2C(0, I2CPins[0], I2CPins[1])

# Create Instances of Sensors
LSObject = LS.LightSensor(I2CObject)
HSObject = HS.HumiditySensor(I2CObject)
PSObject = PS.PressureSensor(I2CObject)
TSObject = TS.TemperatureSensor(30)

sensors = [LSObject, HSObject, PSObject, TSObject]

# Check Status of All Sensors
sensorStatusCheck = []
for i in sensors:
    sensorStatusCheck.append(i.StatusCheck())

# Main Loop
while (
    sensorStatusCheck[0]
    and sensorStatusCheck[1]
    and sensorStatusCheck[2]
    and sensorStatusCheck[3]
):
    time.sleep(1)

    lightData = LSObject.ReadData()
    humidityData = HSObject.read_humidity()
    pressureData = PSObject.ReadData()
    temperatureData = TSObject.read_temperature()

    print(
        f"""Current Sensor Readings
            Temperature: {temperatureData}°C
            Humidity: {humidityData}%
            Light: {lightData}lux
            Pressure: {pressureData}Pa"""
    )
    print("-------------------------------------")
