import os
"""
output = "0b8fb3fe251568e9fd48740faeeb0b34"
output = bytes.fromhex(output)
print(output)
BLOCK_SIZE=16
key = os.urandom(BLOCK_SIZE)

def encrypt(ct, key):
    pt =b''
    j = 0
    for i in range(len(ct)):
        pt += (key[j] ^ ct[i]).to_bytes(1, 'big')
        j+=1
        j%=16
    return pt
print(encrypt(output, key))
output = encrypt(output, key)
def pad_pt(pt):
    amount_padding = 16 if(16 - len(pt) % 16) ==0 else 16 - len(pt) %16
    return pt +(b'\x3f' * amount_padding)
print(pad_pt(output))
"""

enc = "b4b55c3ee34fac488ebeda573ab1f974bf9b2b0ee865e45a92d2f14b7bdabb6ed4872e4dd974e803d9b2ba1c77baf725"
key = [-1 for i in range(16)]
flag_st = "TFCCTF{"
for i in range(len(flag_st)):
    key[i] = ord(flag_st[i])^int(enc[i*2:(i+1)*2],16)

for padlen in range(1,16):
    flag_ed = "}" + "?"*padlen
    tenc = enc[-32:]
    for j in range(16-len(flag_ed),16):
        key[j] = ord(flag_ed[j-16+len(flag_ed)])^int(tenc[j*2:(j+1)*2],16)
    print(f"pad length : {padlen}, ",end="")
    for i in range(len(enc)//2):
        if key[i%16] == -1: print("*",end="")
        else:
            c = key[i%16]^int(enc[i*2:(i+1)*2],16)
            print(chr(c),end="")
    print()
