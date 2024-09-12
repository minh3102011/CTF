import hashlib
import itertools
import os

def S(x, j, n=64):
    j = j % n
    return ((x << j) | (x >> (n - j))) & 0xffffffffffffffff

def key_schedule(k, m, T, z):
    k = k[:]
    for i in range(m, T):
        tmp = S(k[i - 1], -3)
        if m == 4:
            tmp ^= k[i - 3]
        tmp ^= S(tmp, -1)
        zi = (z >> ((i - m) % 62)) & 1
        k.append(k[i - m] ^ tmp ^ zi ^ 0xfffffffffffffffc)
    return k

def simon_encrypt(x, y, k, T):
    for i in range(T):
        tmp = x
        x = y ^ (S(x, 1) & S(x, 8)) ^ S(x, 2) ^ k[i]
        y = tmp
    return x, y

def simon_decrypt(x, y, k, T):
    for i in range(T - 1, -1, -1):
        tmp = y
        y = x ^ (S(y, 1) & S(y, 8)) ^ S(y, 2) ^ k[i]
        x = tmp
    return x, y

def decrypt(ct, k, T):
    pt = bytes()
    for i in range(0, len(ct), 16):
        x = int.from_bytes(ct[i:i+8], 'big')
        y = int.from_bytes(ct[i+8:i+16], 'big')
        x, y = simon_decrypt(x, y, k, T)
        pt += x.to_bytes(8, 'big')
        pt += y.to_bytes(8, 'big')
    return pt
z = 0b01100111000011010100100010111110110011100001101010010001011111
n = 64
m = 4

    # Đọc flag từ file
with open('flag.txt') as f:
    flag = f.read().strip().encode()

    # Khởi tạo khóa
key = [
        0x0f1571c947d9e859, 0x7a5c342c9d8a4286, 
        0xe1e30e24db7f02fb, 0xd4d7c5e0f1230b52
    ]

    # Tạo các khóa con cho từng Simon
k68 = key_schedule(key, m, 68, z)
k69 = key_schedule(key, m, 69, z)
k72 = key_schedule(key, m, 72, z)

    # Mã hóa flag để tạo plaintext đầu vào
pt = flag + bytes(-len(flag) % 16)

    # Mã hóa để kiểm tra
ct68 = simon_encrypt(Simon(key, 68), pt)
ct69 = simon_encrypt(Simon(key, 69), pt)
ct72 = simon_encrypt(Simon(key, 72), pt)

print("Ciphertext for 68 rounds:", ct68.hex())
print("Ciphertext for 69 rounds:", ct69.hex())
print("Ciphertext for 72 rounds:", ct72.hex())

    # Giải mã
decrypted_pt68 = decrypt(ct68, k68, 68)
decrypted_pt69 = decrypt(ct69, k69, 69)
decrypted_pt72 = decrypt(ct72, k72, 72)

print("Decrypted plaintext for 68 rounds:", decrypted_pt68)
print("Decrypted plaintext for 69 rounds:", decrypted_pt69)
print("Decrypted plaintext for 72 rounds:", decrypted_pt72)

