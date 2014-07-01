#!/usr/bin/env python
import numpy
import scipy
import os

def scan():
    pass

def create_image():
    pass
def data_to_str(data):
    s=''
    for i in data:
        s=s+' %d' %i
    return s
    
def save_data(filename):
    if os.path.isfile(filename):
        print filename+'is exist.'
    else:
        fw=open(filename,'w+')
        try:
            fw.write()
        finally:
            fw.close()
        
def save_image(filename):
    if os.path.isfile(filename):
        print filename+'is exist.'
    else
        fw=open(filename,'w+')
        try:
            
        finally:
            fw.close()