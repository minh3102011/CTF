#!/usr/bin/env python3

from random import randint

with open('flag.txt', 'rb') as f:
    flag = f.read()

with open('secret-key.txt', 'rb') as f:
    key = f.read()

def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

ctxt = encrypt(flag, key)

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'break it'
]

for random_str in random_strs:
    for i in range(randint(0, pow(2, 8))):
        for j in range(randint(0, pow(2, 6))):
            for k in range(randint(0, pow(2, 4))):
                for l in range(randint(0, pow(2, 2))):
                    for m in range(randint(0, pow(2, 0))):
                        ctxt = encrypt(ctxt, random_str)
#01101101 01111001 00100000 01100101 01101110 01100011 01110010 01111001 01110000 01110100 01101001 01101111 01101110 00100000 01101101 01100101 01110100 01101000 01101111 01100100
#^
#01110000 01101001 01100011 01101111 01000011 01010100 01000110 01111011 01110111 00110100 00110001 01110100 01011111 01110011 00110000 01011111 00110001 01011111 01100100 00110001 01100100 01101110 01110100 01011111 00110001 01101110 01110110 00110011 01101110 01110100 01011111 01111000 00110000 01110010 00111111 00111111 00111111 01111101
#00011101
with open('output.txt', 'w') as f:
    f.write(ctxt.hex())
