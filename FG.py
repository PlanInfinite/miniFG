import serial

port_in = raw_input('Enter port name: ')
baurd_in = input('Enter baurdrate: ')

ser = serial.Serial(port_in, baurd_in)
