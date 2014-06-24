#!/usr/bin/env python

#COMMAND HEAD
CMD_HEAD={'CMD_COMMUNICATE':'0000','CMD_MOTOR':'0001','CMD_PID':'0002'}

#
CMD_MOTOR={'SET_ORIGIN':'0000','AUTO_APPROACH':'0001','AUTO_WITHDRAW':'0002',
	'STOP':'0003','APPROACH':'0004','WIDTHDRAW':'0005','BACK_TO_ORIGIN':'0006'}

#
CMD_PID={'ENABLE':'0000','SET_P':'0001','SET_I':'0002','SET_D':'0003','DELAY':'0004','SETPOINT':'0005'}

#
CMD_BODY={'CMD_MOTOR':CMD_MOTOR,'CMD_PID':CMD_PID}

DATA_MAX=65535


def cmd_render_2(head,body,data1,data2):
	s='%s%s%04x%04x' %(CMD_HEAD[head],CMD_BODY[head][body],data1,data2)
	return s.decode('hex')

def cmd_render(head,body,data):
	if data>DATA_MAX*2:
		return ''
	elif data>DATA_MAX:
		cmd_render_2(head,body,DATA_MAX,data-DATA_MAx)
	else:
		cmd_render_2(head,body,data,0)
	# s='%s%s%08x' %(CMD_HEAD[head],CMD_BODY[head][body],data)
	# print s.decode('hex')


