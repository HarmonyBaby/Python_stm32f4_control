import commands
import string

motor_help=''
pid_help=''

		# print len(cmd_head)
		# print len(cmd_params)
def control(a):
# 		cmds=argv.lower().split('-')
# 		cmd_head=cmds.pop(0).strip()
# 		cmd_params=cmds
# 		if cmd_head=='exit' or cmd_head=='quit':
# 			break	
# 		elif cmd_head=='motor':
# 			control.motor_control(cmd_params)	
# 		elif cmd_head=='pid':
# 			control.PID_control(cmd_params)
# 		elif cmd_head=='dds':
# 			control.DDS_control(cmd_params)	
# 		else:
# 			print 'bad command'
# 			continue
	pass
def cmd_preprocess(cmd_param):
		c=cmd_param.split()
		if len(c)==2:
			return c[0],string.atoi(c[1])
		elif len(c)==1:
			return c[0],0
		else:
			return 'error',0		

def motor_control(cmds):
	if(len(cmds)==0):
		print motor_help;
	else:
		for cmd in cmds:
			k,v=cmd_preprocess(cmd)
			if k=='approach' or k=='ap':
				commands.cmd_execute('CMD_MOTOR','APPROACH',v)
			elif k=='withdraw' or k=='wd':
				commands.cmd_execute('CMD_MOTOR','WIDTHDRAW',v)
			elif k=='setorigin' or k=='so':
				commands.cmd_execute('CMD_MOTOR','SET_ORIGIN',v)
			elif k=='backtoorigin' or k=='bo':
				commands.cmd_execute('CMD_MOTOR','BACK_TO_ORIGIN',0)
			elif k=='autoapproach' or k=='aa':
				commands.cmd_execute('CMD_MOTOR','AUTO_APPROACH',0)
			elif k=='autowithdraw' or k=='aw':
				commands.cmd_execute('CMD_MOTOR','AUTO_WITHDRAW',0)
			elif k=='stop' or k=='st':
				commands.cmd_execute('CMD_MOTOR','STOP',0)
			else:
				print 'bad command %s' %(k)

def PID_control(cmds):
	if(len(cmds)==0):
		print pid_help;
	else:
		for cmd in cmds:
			k,v=cmd_preprocess(cmd)
			if k=='setp' or k=='sp':
				commands.cmd_execute('CMD_PID','SET_P',v)
			elif k=='seti' or k=='si':
				commands.cmd_execute('CMD_PID','SET_I',v)
			elif k=='setd' or k=='sd':
				commands.cmd_execute('CMD_PID','SET_D',v)
			elif k=='delay' or k=='de':
				commands.cmd_execute('CMD_PID','SETPOINT',v)		
			elif k=='enable' or k=='en':
				commands.cmd_execute('CMD_PID','ENABLE',0)
			else:
				print 'bad command %s' %(k)

def DDS_control(cmds):
	return