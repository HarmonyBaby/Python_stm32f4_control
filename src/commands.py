#!/usr/bin/env python
import myserial

#COMMAND HEAD
CMD_HEAD={
		'CMD_COMMUNICATE':	'0001',
		'CMD_MOTOR':					'0002',
		'CMD_PID':						'0003',
		'CMD_DDS':						'0004',
		'CMD_SCAN':					'0010'
		}

#
CMD_MOTOR={
		'SET_ORIGIN':					'0000',
		'AUTO_APPROACH':		'0001',
		'AUTO_WITHDRAW':		'0002',
		'STOP':								'0003',
		'APPROACH':					'0004',
		'WIDTHDRAW':					'0005',
		'BACK_TO_ORIGIN':			'0006'
		}

#
CMD_PID={
		'ENABLE':							'0000',
		'SET_P':								'0001',
		'SET_I':								'0002',
		'SET_D':								'0003',
		'DELAY':								'0004',
		'SETPOINT':						'0005'
		}

#
CMD_DDS={
		'SET_FREQ':						'0001',
		'SET_START_FREQ':		'0002',
		'SET_END_FREQ':			'0003',
		'SET_POINTS':					'0004',
		'SWEEP':							'0005',
# 		'START':								'0006'
		}

#
CMD_SCAN={
		'START':								'0001'
		}
#
CMD_BODY={
		'CMD_MOTOR':					CMD_MOTOR,
		'CMD_PID':						CMD_PID,
		'CMD_DDS':						CMD_DDS,
		'CMD_SCAN':					CMD_SCAN
		}

DATA_MAX=65535


def cmd_execute_2(head,body,data1,data2):
	s='%s%s%04x%04x' %(CMD_HEAD[head],CMD_BODY[head][body],data1,data2)
# 	myserial.write( s.decode('hex'))
	myserial.write(s)

def cmd_execute(head,body,data):
	if data>DATA_MAX*2:
		print 'Input %d is larger than %d' %(data,DATA_MAX*2)
	elif data>DATA_MAX:
		cmd_execute_2(head,body,DATA_MAX,data-DATA_MAX)
	else:
		cmd_execute_2(head,body,data,0)
	# s='%s%s%08x' %(CMD_HEAD[head],CMD_BODY[head][body],data)
	# print s.decode('hex')


