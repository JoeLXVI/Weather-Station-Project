"""
File Name: WeatherStation_PressureSensor_V1.py
Author: Sam Young (SY947)
Date Created: 26/11/2024
Last Modified:
Description: This code defines a class for a pressure sensor including attributes and methods to allow for the reading and display of sensor data.
"""

# Import Required Modules
import time
import machine


# Define Class
class PressureSensor:

    # Define Constants
    RegistersDictionary = {"Command": 0x06, "PressureData": 0x00}

    # Define Initiation Method
    def __init__(self, I2C, address=0x63):
        self.I2C = I2C
        self.address = address

    # Create Method to Read the Pressure Data from the Sensor
    def ReadData(self):
        self.I2C.writeto_mem(self.address, bytearray([0x30, 0x0A]))
        time.sleep(0.01)
        data = self.I2C.readfrom_mem(
            self.address, self.RegistersDictionary["PressureData"], 4
        )  # Reading 4 Bytes of data
        raw_data = int.from_bytes(data[1:4], "big")
        return raw_data * 100 / 64000.0  # Return pressure in Pascals

    # Create Methods to Power Up and Down
    def PowerDown(self):
        ReadRegister = self.I2C.readfrom_mem(
            self.address, self.RegistersDictionary["Command"], 1
        )[0]
        ReadRegister &= 0xFE  # Set bit 0 to 0 (standby mode)
        self.I2C.writeto_mem(
            self.address, self.RegistersDictionary["Command"], bytearray([ReadRegister])
        )

    def PowerUp(self):
        ReadRegister = self.I2C.readfrom_mem(
            self.address, self.RegistersDictionary["Command"], 1
        )[0]
        ReadRegister |= 0x01  # set bit 0 (Power Definition bit) to 1 (power up)
        self.I2C.writeto_mem(
            self.address, self.RegistersDictionary["Command"], bytearray([ReadRegister])
        )

    # Create Status Check
    def StatusCheck(self):
        # Use a 'Try-Except' block to handle any errors that may occur without the code stopping
        try:
            data = self.I2C.readfrom_mem(
                self.address, self.RegistersDictionary["Command"], 1
            )[0]
            # Check if the sensor is outputting data correctly
            if bool(data & 0x01):
                print("ICP-10100: Sensor Responding")
                return True
            else:
                print("ICP-10100: Invalid Humidity Data")
                return False
        # Handle any errors that occur
        except Exception as e:
            print(f"ICP-10100 Error: {e}")
            return False
