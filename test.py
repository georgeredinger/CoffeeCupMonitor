#!/usr/bin/env python
#based on  http://www.ladyada.net/make/tweetawatt/parser.html
import serial
from xbee import XBee
import time

SERIALPORT = "/dev/ttyUSB0" 
BAUDRATE = 9600     

ser = serial.Serial(SERIALPORT, BAUDRATE)
xbee = XBee(ser)
#ser.open()
#scale factor = (vref)/(max counts)
scalefactor = 2800.0/1023.0
while True:
  response = xbee.wait_read_frame()
  raw = float(response['samples'][0].values()[0])
  volts = (raw*scalefactor)
  print volts/10.0
ser.close()

