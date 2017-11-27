import gdb
import string
from time import sleep
char_set = string.ascii_letters + string.digits + "!_}"
flag = "TUCTF{"

gdb.execute("b *0x0000000000401c82")

while True:
	for c in char_set:
		pattern = flag + c + "A" * (55-len(flag))
		gdb.execute("r {}".format(pattern))
		for i in range(len(flag)):
			gdb.execute("c")
		rax = gdb.execute("p/x $rax",True,True).split()[-1]
		if rax == "0x0":
		 	flag += c
		 	if "}" in flag:
		 		print("Flag : %s" % (flag))
		 		exit(0)
		 	print("Curret Flag : %s" % (flag))
		 	sleep(10)
		 	break
		print("Pattern : %s" % (pattern))
		print("Nilai Rax : %s" % (rax))	

