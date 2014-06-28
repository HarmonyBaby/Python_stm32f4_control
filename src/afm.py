#!/usr/bin/env python

import sys
import afm_control

def run(argv):
	afm_control.run(argv)
	
def interactive_run():
	while True:
		argv=raw_input('Please input the command:')
		argv=argv.lower().strip()
		if argv.startswith('exit') or argv.startswith('quit'):
			exit()
		afm_control.run(argv)
			
if	__name__ =='__main__':
	if len(sys.argv)!=1:
		argv=sys.argv
		argv.pop(0)
		run(argv)
	else:
		interactive_run()



