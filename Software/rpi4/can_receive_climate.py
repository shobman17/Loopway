import can
import struct

# Declare can bus
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Declare a simple bufferedreader to push all messages to a queue
notifier = can.Notifier(bus, [can.BufferedReader()])

while(True):
    msg = notifier.listeners[0].get_message()
    if msg is not None:
        if msg.dlc == 4:
            # message received only has humidity
            h = struct.unpack('f',msg.data)[0]
            print(f"Received - Humidity: {h}%")
        elif msg.dlc == 8:
            tp = struct.unpack('ff',msg.data)
            print(f"Received - Temperature: {tp[0]}C Pressure: {tp[1]} Pa")
        else:
            print("huh?!?!?")
