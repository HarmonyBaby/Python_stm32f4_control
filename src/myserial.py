#!/usr/bin/env python

import serial

m_serial = serial.Serial('/dev/ttyUSB0',115200)  

def serial_write(s):
    m_serial.write(s)


