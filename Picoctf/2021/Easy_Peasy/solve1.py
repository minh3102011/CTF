from pwn import *

KEY_LEN = 50000
MAX_CHUNK = 1000
r = remote('mercury.picoctf.net', 36981)
r.recvuntil('This is the encrypted flag!\n')
flag = r.recvlineS(keepends=False)
log.info(f'Flag: {flag}')
bin_flag = unhex(flag)
log.info(f'bin_flag: {bin_flag}')
counter = KEY_LEN - len(bin_flag)
log.info(f'counter: {counter}')
