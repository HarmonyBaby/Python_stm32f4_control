#!/usr/bin/env python
import sys
import afm_control

def argv_process(argv):
	afm_control.run(argv)

if	__name__ =='__main__':
	if len(sys.argv)!=1:
		argv=sys.argv
		argv.pop(0)
		argv_process(argv)
	else:
		while True:
			argv=raw_input('Please input the command:')
			argv=argv.lower().strip()
			if argv.startswith('exit') or argv.startswith('quit'):
				exit()
			argv_process(argv)



