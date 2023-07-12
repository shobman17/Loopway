# Sample code to keep sending data from the bme280 sensor to the BCU computer

from MCP2512 import MCP2515
from bme280 import BME280
from machine import Pin, SPI, I2C
import time
from array import array
import ustruct

spi_bus = SPI(0, miso = Pin(16), mosi = Pin(19), sck = Pin(18))
cs = Pin(17, Pin.OUT)
interrupt = Pin(20, Pin.IN)

i2c_bus = I2C(0, sda = Pin(4), scl = Pin(5))

can = MCP2515(spi_bus, cs)
print("Initialising CAN bus")
can.Init()
print("CAN bus init done")
idbus = 0x123

bme = BME280(i2c = i2c_bus)
TPH = array("f",[0,0,0]) # To avoid accessing the memory heap during every call
while(True):
    bme.read_compensated_data(TPH)
    print(f"Temp: {TPH[0]} Pressure: {TPH[1]} Humidity: {TPH[2]}")
    tp = ustruct.pack('ff',TPH[0], TPH[1])
    h = ustruct.pack('f',TPH[2])
    print("Sending temp & pressure")
    can.Send(idbus, tp, 8)
    print("Sending humidity")
    can.Send(idbus,h,4)
    time.sleep(0.5)
 