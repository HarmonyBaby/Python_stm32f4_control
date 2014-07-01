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
			break
		afm_control.run(argv)

if	__name__ =='__main__':
	import afm_data_correction as afmio
	import afm_image_display as disp
	
	data=afmio.read_data('1.rawdata')
	disp.plot_3d(data)
# 	if len(sys.argv)!=1:
# 		argv=sys.argv
# 		argv.pop(0)
# 		run(argv)
# 	else:
# 		interactive_run()



