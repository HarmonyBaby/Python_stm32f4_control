#!/usr/bin/env python
import string
import myserial
import control

while True:
	cmd=raw_input('Please input the command:')
	cmds=cmd.lower().split('-')
	cmd_head=cmds.pop(0).strip()
	cmd_params=cmds.strip()
	# print len(cmd_head)
	# print len(cmd_params)

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


