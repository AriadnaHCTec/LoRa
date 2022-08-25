"""
Made by:Ariadna Huesca Coronado
	A01749161@tec.mx
	arihuescac@hotmail.com
Modified (DD/MM/YY): 
	Ariadna Huesca  17/08/2022 Creation
"""
import serial
import time
ser = serial.Serial('/dev/ttyACM0')  # open serial port
ser.baudrate = 9600
while True:
    a = str(input("que quieres mandar: "))
    ser.write(bytes(a,'utf-8'))
    time.sleep(3)
ser.close()    
