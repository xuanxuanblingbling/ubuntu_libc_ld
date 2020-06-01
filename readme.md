# 常见的ubuntu中的ld与libc收集

用于做Pwn题时不同的环境：

```python
from pwn import *
context(arch='amd64',os='linux',log_level='debug')
myelf  = ELF("./note")
libc   = ELF("./x64/2.29/libc-2.29.so")
ld     = ELF("./x64/2.29/ld-2.29.so")
io     = process(argv=[ld.path,myelf.path],env={"LD_PRELOAD" : libc.path})
gdb.attach(io,"vmmap")
io.interactive()
```

内存布局如下：

```c
Start              End                Offset             Perm Path
0x00007f7359cdf000 0x00007f7359d04000 0x0000000000000000 r-- /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/libc-2.29.so
0x00007f7359d04000 0x00007f7359e7c000 0x0000000000025000 r-x /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/libc-2.29.so
0x00007f7359e7c000 0x00007f7359ec5000 0x000000000019d000 r-- /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/libc-2.29.so
0x00007f7359ec5000 0x00007f7359ec8000 0x00000000001e5000 r-- /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/libc-2.29.so
0x00007f7359ec8000 0x00007f7359ecb000 0x00000000001e8000 rw- /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/libc-2.29.so
0x00007f7359ecb000 0x00007f7359ed1000 0x0000000000000000 rw- 
0x00007f7359ed1000 0x00007f7359ed2000 0x0000000000000000 r-- /mnt/hgfs/桌面/pwn/libc/github/note
0x00007f7359ed2000 0x00007f7359ed3000 0x0000000000001000 r-x /mnt/hgfs/桌面/pwn/libc/github/note
0x00007f7359ed3000 0x00007f7359ed4000 0x0000000000002000 r-- /mnt/hgfs/桌面/pwn/libc/github/note
0x00007f7359ed4000 0x00007f7359ed5000 0x0000000000002000 r-- /mnt/hgfs/桌面/pwn/libc/github/note
0x00007f7359ed5000 0x00007f7359ed6000 0x0000000000003000 rw- /mnt/hgfs/桌面/pwn/libc/github/note
0x00007f7359ed6000 0x00007f7359ed7000 0x0000000000000000 r-- /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/ld-2.29.so
0x00007f7359ed7000 0x00007f7359efa000 0x0000000000001000 r-x /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/ld-2.29.so
0x00007f7359efa000 0x00007f7359f02000 0x0000000000024000 r-- /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/ld-2.29.so
0x00007f7359f03000 0x00007f7359f04000 0x000000000002c000 r-- /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/ld-2.29.so
0x00007f7359f04000 0x00007f7359f05000 0x000000000002d000 rw- /mnt/hgfs/桌面/pwn/libc/github/x64/2.29/ld-2.29.so
0x00007f7359f05000 0x00007f7359f06000 0x0000000000000000 rw- 
0x00007ffcf30c0000 0x00007ffcf30e1000 0x0000000000000000 rw- [stack]
0x00007ffcf3198000 0x00007ffcf319b000 0x0000000000000000 r-- [vvar]
0x00007ffcf319b000 0x00007ffcf319d000 0x0000000000000000 r-x [vdso]
0xffffffffff600000 0xffffffffff601000 0x0000000000000000 r-x [vsyscall]
```
