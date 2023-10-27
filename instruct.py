import serial
import time

ser = serial.Serial('COM4', 9600, timeout=0)
while 1:
    var = input("Enter:")
    var+='\n'
    print(str.encode(var))
    ser.write(str.encode(var))
    time.sleep(0.5)
    print(ser.readline()[:-2])#.decode('utf-8'))