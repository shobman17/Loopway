from MCP2512 import MCP2515
from machine import Pin, SPI
import time

spi_bus = SPI(0, miso = Pin(16), mosi = Pin(19), sck = Pin(18))
spi_bus_no = SPI(1)
cs = Pin(17, Pin.OUT)
interrupt = Pin(20, Pin.IN)

can = MCP2515(spi_bus, cs)
print("init...")
can.Init()

# CAN_WRITE = 0x02
# CAN_READ = 0x03
# cs(0)
# spi_bus.write(bytearray([CAN_READ,0x0E]))
# res = spi_bus.read(1)
# cs(1)
# print(res)

idbus = 0x123 #max 7ff
data = [0,1,2,3,4,5,7,8]
dlc = 8
while(True):
    print("send data...")
    can.Send(idbus, data, dlc)
    time.sleep(1)

# readbuf = []
# while(1):
#     readbuf = can.Receive(id)
#     print('reading...')
#     print(readbuf)
#     time.sleep(0.5)


# if __name__ == '__main__':
# 	print("--------------------------------------------------------")
# 	can = MCP2515()
# 	print("init...")
# 	can.Init()
# 	print("send data...")
# 	id = 0x123 #max 7ff
# 	data = [1, 2, 3, 4, 5, 6, 7, 8]
# 	dlc = 8
# 	can.Send(id, data, dlc)
# 
# 	readbuf = []
# 	# while(1):
# 	while(1):
# 		readbuf = can.Receive(id)
# 		print(readbuf)
# 		time.sleep(0.5)
# 
# 	print("--------------------------------------------------------")