import serial
import time

# set microbit port
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2) # stay connecting

print("1: smile(go), 0: sad(stop), q: quit")

while True:
    val = input("input command: ")
    if val == 'q':
        break

    ser.write(val.encode()) # sending data to microbit

ser.close()
