#!/usr/bin/env python
# import string
import control_modules as controller
import myserial

def run(argv):
	cmds=argv.lower().split('-')
	cmd_head=cmds.pop(0).strip()
	cmd_params=cmds
	if cmd_head=='serial':
		myserial.serial_set(cmd_params)
	if controller.control_funcs.has_key(cmd_head):
		controller.control_funcs[cmd_head](cmd_params)
	else:
		print 'Bad command: "%s"' %cmd_head
		funcs=controller.control_funcs.keys()
		funcs.insert(0,'serial')
		print 'Avaliable commands: %s' %funcs
		
		
# 	if cmd_head=='motor':
# 		controller.motor_control(cmd_params)	
# 	elif cmd_head=='pid':
# 		controller.PID_control(cmd_params)
# 	elif cmd_head=='dds':
# 		controller.DDS_control(cmd_params)
# 	elif cmd_head=='scan':
# 		controller.scan_control(cmd_params)	
# 	else:
# 		print 'Bad command: "%s"' %cmd_head
# 		print 'Avaliable commands:"motor","pid","dds","scan"'
	


