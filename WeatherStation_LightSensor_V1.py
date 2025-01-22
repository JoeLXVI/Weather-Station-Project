""" 
File Name: WeatherStation_LightSensor_V1.py
Author: Robbie Votta (RV434)
Date Created: 26/11/2024
Last Modified: 
Description: This code defines a class for a light sensor including attributes and methods to allow for the reading and display of sensor data.
"""

import time
import machine


class LightSensor:  #
    ConversionFactor = 0.0576
    CommandRegister = 0x00
    HighByte = 0x04
    LowByte = 0x05

    def __init__(self, I2C):
        self.I2C = I2C
        self.address = 0x10
        self.WriteRegsiter(self.CommandRegister, 0x0000)

    def WriteRegister(self, register, payload):
        data = bytearray([(payload & 0xFF), ((payload >> 8) & 0xFF)])
        self.I2C.writeto_mem(self.address, register, data)

    def ReadRegister(self, register, length=2):
        self.I2C.readfrom_mem(self.address, register, length)
        return int.from_bytes(data, "little")

    def ReadData(self):
        LowData = ReadRegister(self.LowByte, 1)
        HighData = ReadRegister(self.HighByte, 1)
        CombinedData = (HighData << 8) | LowData
        lux = CombinedData * self.ConversionFactor
        return lux

    def configure(self, settings):
        self.WriteRegister(self.CommandRegister, settings)

    def PowerDown(self):
        self.WriteRegister(self.CommandRegister, 0x01)

    def PowerUp(self):
        self.WriteRegsiter(self.CommandRegister, 0x0000)
