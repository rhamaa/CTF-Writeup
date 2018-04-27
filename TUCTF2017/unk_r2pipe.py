import r2pipe
import string
import sys
from time import sleep

char_set = string.ascii_letters + string.digits + "!_}"

flag = "TUCTF{"
r2 = r2pipe.open("/tmp/unknown")

def write(data):
	sys.stdout.write(data)
	sys.stdout.flush()

while True:
	for c in char_set:
		pattern = flag + c + "A" * (55-len(flag))
		r2.cmd('doo "{}"'.format("".join(pattern)))
		r2.cmd("db 0x401C82")
		for i in range(len(flag)+1):
			r2.cmd("dc")
		rax = int(r2.cmd("dr rax"), 16)
		if rax == 0:
			flag += c
			write("Current Flag : {}\n".format(flag))
			write("Current Pattern : {}\n".format(pattern))
			if "}" in flag:
				write("Flag : {}\n".format(flag))
				write("Flag : {}\n".format(flag))
				exit(0)
			# sleep(5)