
import serial
import time
import sys

ser = serial.Serial('COM4', 9600, timeout=0)

var = input("Enter:")
print(sys.getsizeof(var))
var = 'RUN'
#print(type(var))
var+='\n'
print(sys.getsizeof(var))
print(str.encode(var))
ser.write(str.encode(var))
time.sleep(0.5)
print(ser.readline()[:-2])#.decode('utf-8'))
