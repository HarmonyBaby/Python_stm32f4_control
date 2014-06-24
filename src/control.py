import commands

motor_help=''
pid_help=''

def cmd_preprocess(cmd_params):
		for c in cmd_params:
		c=c.split()
		if len(c)==2:
			cmd_params[c[0]]=string.atoi(c[1])
		elif len(c)==1:
			cmd_params[c[0]]=0
		else:
			cmd_head='error'

def motor_control(cmds):
	if(len(cmds)==0):
		print motor_help;
	else:
		for k,v in cmds.items():
			if k=='approach' or k=='ap':
				commands.cmd_render('CMD_MOTOR','APPROACH',v)
			elif k=='withdraw' or k=='wd':
				commands.cmd_render('CMD_MOTOR','WIDTHDRAW',v)
			elif k=='setorigin' or k=='so':
				commands.cmd_render('CMD_MOTOR','SET_ORIGIN',v)
			elif k=='backtoorigin' or k=='bo':
				commands.cmd_render('CMD_MOTOR','BACK_TO_ORIGIN',0)
			elif k=='autoapproach' or k=='aa':
				commands.cmd_render('CMD_MOTOR','AUTO_APPROACH',0)
			elif k=='autowithdraw' or k=='aw':
				commands.cmd_render('CMD_MOTOR','AUTO_WITHDRAW',0)
			elif k=='stop' or k=='st':
				commands.cmd_render('CMD_MOTOR','STOP',0)
			else:
				print 'bad command %s' %(k)

def PID_control(cmds):
	if(len(cmds)==0):
		print pid_help;
	else:
		for (k,v) in cmds.items():
			if k=='setp' or k=='sp':
				commands.cmd_render('CMD_PID','SET_P',v)
			elif k=='seti' or k=='si':
				commands.cmd_render('CMD_PID','SET_I',v)
			elif k=='setd' or k=='sd':
				commands.cmd_render('CMD_PID','SET_D',v)
			elif k=='delay' or k=='de':
				commands.cmd_render('CMD_PID','SETPOINT',v)		
			elif k=='enable' or k=='en':
				commands.cmd_render('CMD_PID','ENABLE',0)
			else:
				print 'bad command %s' %(k)

def DDS_control(cmds):
	return