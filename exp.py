from pwn import *
context(arch='amd64',os='linux',log_level='debug')
myelf  = ELF("./note")
libc   = ELF("./x64/2.29/libc-2.29.so")
ld     = ELF("./x64/2.29/ld-2.29.so")
io     = process(argv=[ld.path,myelf.path],env={"LD_PRELOAD" : libc.path})
gdb.attach(io,"vmmap")
io.interactive()