import sys
from platform import architecture
if architecture()[0]=='64bit':
	import dump
	sys.exit()
else:sys.exit('\033[1;31mYour device not supported, \033[33m64bit is required\033[0m')
