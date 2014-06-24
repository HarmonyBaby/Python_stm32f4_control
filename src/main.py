#!/usr/bin/env python

import myserial
import settings
import control

def Error():
	pass

while True:

	cmd=raw_input('Please input the command:')
	cmds=cmd.lower().split('-')

	cmd_head=cmds.pop(0).strip()
	cmd_params=dict()
	# print len(cmd_head)
	# print len(cmd_params)
	for c in cmds:
		c=c.split()
		if len(c)==2:
			dict[c[0]]=c[1]
		elif len(c)==1:
			dict[c[0]]=0
		else:
			cmd_head='error'


	if cmd_head=='exit' or cmd_head=='quit':
		break
	
	elif cmd_head=='motor':
		control.motor_control(cmd_params)
	
	elif cmd_head=='pid':
		control.PID_control(cmd_params)

	elif cmd_head=='dds':
		control.DDS_control(cmd_params)
	
	else:
		print 'bad command'
		continue


