#!/usr/bin/env python
import pickle
import serial
import os
import sys

filename='myserial.settings'
fullpath=''
myserial_settings=dict()
myserial_settings['port']='/dev/ttyUSB1'
myserial_settings['baudrate']=115200

def write(m_serial,s):
    m_serial.write(s)

def save_settings():
    fullpath=os.path.join(sys.path[0],filename)
    f = open(fullpath,"w")
    pickle.dump(myserial_settings, f)
    f.close()   

def load_settings():
    fullpath=os.path.join(sys.path[0],filename)
    if os.path.isfile(fullpath):
        f = open(fullpath,"r")
        myserial_settings=pickle.load(f)
        f.close()
    else:
        save_settings()
    port_info()

def open_port():
    return serial.Serial(myserial_settings['port'],myserial_settings['baudrate'])

def close_port(m_serial):
    m_serial.close()

def set_port(port,baudrate):
    myserial_settings['port']=port
    myserial_settings['baudrate']=baudrate
    save_settings()
    port_info()

def port_info():
    print myserial_settings

if __name__=='__main__':
    if  len(sys.argv)==1:
        load_settings()
    elif len(sys.argv)==3:
        set_port(sys.argv[1],sys.argv[2])
    else:
        print 'You should input two parameters:portname and baudrate.'
