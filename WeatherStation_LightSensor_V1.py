""" 
File Name: WeatherStation_LightSensor_V1.py
Author: Robbie Votta (RV434)
Date Created: 26/11/2024
Last Modified: 22/01/2025
Description: This code defines a class for a light sensor including attributes and methods to allow for the reading and display of sensor data.
"""

# Import Required Modules
import time
import machine


# Define Class
class LightSensor:

    # Define Constants
    ConversionFactor = 0.0576
    RegistersDictionary = {"Command": 0x00, "HighByte": 0x04, "LowByte": 0x05}

    # Define Initiation Method
    def __init__(self, I2C):
        self.I2C = I2C
        self.address = 0x10
        self.WriteRegsiter(self.RegistersDictionary["Command"], 0x0000)

    # Create Method to Write to the Sensors Registers
    def WriteRegister(self, register, payload):
        data = bytearray([(payload & 0xFF), ((payload >> 8) & 0xFF)])
        self.I2C.writeto_mem(self.address, register, data)

    # Create Method to Read from the Sensors Registers
    def ReadRegister(self, register, length=2):
        data = self.I2C.readfrom_mem(self.address, register, length)
        return int.from_bytes(data, "little")

    # Create Method to Read the Light Data from the Sensor
    def ReadData(self):
        LowData = self.ReadRegister(self.RegistersDictionary["LowByte"], 1)
        HighData = self.ReadRegister(self.RegistersDictionary["HighByte"], 1)
        CombinedData = (HighData << 8) | LowData
        lux = CombinedData * self.ConversionFactor
        return lux

    # Create Method to Change Sensor Configuration
    def configure(self, settings):
        self.WriteRegister(self.RegistersDictionary["Command"], settings)

    # Create Methods to Power Up and Down
    def PowerDown(self):
        self.WriteRegister(self.RegistersDictionary["Command"], 0x01)

    def PowerUp(self):
        self.WriteRegsiter(self.RegistersDictionary["Command"], 0x0000)

    # Create Status Check
    def StatusCheck(self):
        # Use a 'Try-Except' block to handle any errors that may occur without the code stopping
        try:
            data = self.ReadData
            # Check if the sensor is outputting data correctly
            if data >= 0:
                print("VEML6031: Sensor Responding")
                return True
            else:
                print("VEML6031: Invalid Light Data")
                return False
        # Handle any errors that occur
        except Exception as e:
            print(f"VEML6031 Error: {e}")
            return False
