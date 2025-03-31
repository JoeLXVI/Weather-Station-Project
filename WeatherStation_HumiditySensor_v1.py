"""
File Name: WeatherStation_HumiditySensor_V1.py
Author: Mlles Perandin-Grainger (MPG54)
Date Created: 26/11/2024
Last Modified:
Description: This code defines a class for a humidity sensor including attributes and methods to allow for the reading and display of sensor data.
"""

# Import Required Modules
import time
import machine


# Define Class
class HumiditySensor:

    # Define Constants
    RegistersDictionary = {"Command": 0x20, "HumidityData": 0x28}

    # Define Initiation Method
    def __init__(self, I2C, address=0x5F):
        self.I2C = I2C
        self.address = address

    # Create Method to Read the Light Data from the Sensor
    def ReadData(self):
        raw_data = self.I2C.read_from_mem(
            self.address, self.RegistersDictionary["HumidityData"], 2
        )
        return int.from_bytes(raw_data, "little")

    def read_humidity(self):
        raw_data = self.ReadData()
        return raw_data / 16.0  # formula from datasheet

    # Create Methods to Power Up and Down
    def PowerDown(self):
        ReadRegister = self.I2C.readfrom_mem(
            self.address, self.RegistersDictionary["Command"], 1
        )[0]
        ReadRegister |= 0x80  # set bit 7 (Power Definition bit) to 1 (power up)
        self.I2C.writeto_mem(
            self.address, self.RegistersDictionary["Command"], bytearray([ReadRegister])
        )

    def PowerUp(self):
        ReadRegister = self.I2C.readfrom_mem(
            self.address, self.RegistersDictionary["Command"], 1
        )[0]
        ReadRegister |= 0x80  # set bit 7 (Power Definition bit) to 1 (power up)
        self.I2C.writeto_mem(
            self.address, self.RegistersDictionary["Command"], bytearray([ReadRegister])
        )

    # Create Status Check
    def StatusCheck(self):
        # Use a 'Try-Except' block to handle any errors that may occur without the code stopping
        try:
            data = self.I2C.readfrom_mem(
                self.address, self.RegistersDictionary["Status"], 1
            )[0]
            # Check if the sensor is outputting data correctly
            if bool(data & 0x02):
                print("WSEN-HIDS: Sensor Responding")
                return True
            else:
                print("WSEN-HIDS: Invalid Humidity Data")
                return False
        # Handle any errors that occur
        except Exception as e:
            print(f"WSEN-HIDS Error: {e}")
            return False
