import commands

motor_help=''


def motor_control(cmds):
	if(len(cmds)==0):
		print motor_help;
	else:
		for k,v in cmds:
			if k=='approach' or k=='ap':
				 commands.cmd_render_2('CMD_MOTOR','APPROACH',v)
			elif k=='withdraw' or k=='wd':
				commands.cmd_render_2('CMD_MOTOR','WIDTHDRAW',v)
			elif k=='setorigin' or k=='so':
				commands.cmd_render_2('CMD_MOTOR','SET_ORIGIN',v)
			elif k=='backtoorigin' or k=='bo':
				commands.cmd_render('CMD_MOTOR','BACK_TO_ORIGIN',0)
			elif k=='autoapproach' or k=='aa':
				commands.cmd_render('CMD_MOTOR','AUTO_APPROACH',0)
			elif k=='autowithdraw' or k=='aw':
				commands.cmd_render('CMD_MOTOR','AUTO_WITHDRAW',0)
			elif k=='stop' or k=='st':
				commands.cmd_render('CMD_MOTOR','STOP',0)
			else:
				return 'bad command'
			return 'ok'

def PID_control(cmds):
	if(len(cmds)==0):
		print motor_help;
	else:
		for k,v in cmds:
			if k=='setp' or k=='sp':
				commands.cmd_render('CMD_PID','SET_P',v)
			if k=='seti' or k=='si':
				commands.cmd_render('CMD_PID','SET_I',v)
			if k=='setd' or k=='sd':
				commands.cmd_render('CMD_PID','SET_D',v)
			if k=='delay' or k=='de':
				commands.cmd_render('CMD_PID','SETPOINT',v)		
			if k=='enable' or k=='en':
				commands.cmd_render('CMD_PID','ENABLE',0)
			else:
				return 'bad command'
			return 'ok'

def DDS_control(cmds):
	return