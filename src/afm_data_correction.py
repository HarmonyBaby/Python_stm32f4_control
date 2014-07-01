#!/usr/bin/env python
import sys
import os
import string
import numpy as np

num_err=10

def str_to_array(dataline):
	str_array=dataline.split()
	size=len(str_array)
	num_array=np.zeros(size,dtype=np.int32)
	i=0
	while i<size:
		num_array[i]=string.atoi(str_array[i])
		i=i+1
	return num_array
def array_to_str(array):
	s=''
	for i in array:
		s=s+'%d ' %i
	s.strip()
	return s

def read_data(filepath):
	fid=open(filepath,'r')
	raw_datalines=fid.readlines()
	fid.close()
	size=len(raw_datalines)
	data=np.zeros((size,size),dtype=np.int32)
	i=0
	while i<size:
		data[i,:]=str_to_array(raw_datalines[i])
		i=i+1
	return data
#  	print data.shape

def write_data(filepath,data):
	fid=open(filepath,'w')
	print data
	i=0
	while i<data.shape[0]:
		fid.write(array_to_str(data[i,:]))
		fid.write('\r\n')
		i=i+1
	fid.close()

def correction(raw_data):
	correction_data=np.zeros(raw_data.shape,np.int32)
	size=raw_data.shape[0]
	correction_data[0:size,0:size-num_err]= raw_data[0:size,num_err:size]
	correction_data[0:size-1,size-num_err:size]=raw_data[1:size,0:num_err]
	correction_data[size-1,size-num_err:size]=correction_data[size-2,size-num_err:size]
	return correction_data

if __name__=='__main__':
	if len(sys.argv)!=3:
		print 'Two parameters expected:"input filename and output filename."'
		exit()
	fi=sys.argv[1]
	fo=sys.argv[2]
	if not os.path.isfile(fi):
		print '%s is not a right file path.' %fi
		exit()
	if os.path.isfile(fo):
		print '%s is exist' %fo
		exit()
	data=read_data(fi)
	correction_data=correction(data)
	write_data(fo,correction_data)
