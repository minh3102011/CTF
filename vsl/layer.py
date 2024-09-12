"""
import hashlib
import itertools
import os
def xor(key, data):
    return bytes([k ^ d for k, d in zip(itertools.cycle(key), data)])

def decrypt(phrase, encrypted_message, iters=1000):
    key = phrase.encode()
    keys = []
    for _ in range(iters):
        key = hashlib.md5(key).digest()
        keys.append(key)
    
    for key in reversed(keys):
        encrypted_message = xor(key, encrypted_message)
    
    return encrypted_message

# Thông điệp mã hóa từ dịch vụ
encrypted_flag_hex = input("Enter the encrypted flag (hex) > ")
encrypted_flag = bytes.fromhex(encrypted_flag_hex)

# Mật khẩu (FLAG)
phrase = os.environ.get('FLAG', 'missing')

# Giải mã thông điệp
decrypted_flag = decrypt(phrase, encrypted_flag)
print(decrypted_flag.decode())
"""
import hashlib
import itertools
import os

def xor(key, data):
    return bytes([k ^ d for k, d in zip(itertools.cycle(key), data)])

def decrypt(phrase, encrypted_message, iters=1000):
    key = phrase.encode()
    keys = []
    for _ in range(iters):
        key = hashlib.md5(key).digest()
        keys.append(key)
    
    for key in reversed(keys):
        encrypted_message = xor(key, encrypted_message)
    
    return encrypted_message

# Thông điệp mã hóa từ dịch vụ
encrypted_flag_hex = "fb7fdbf9e714a08ce9cdf109bb527acba27accfeff16fcdcb1cdf358bb557898aa2d9da9af5c"
encrypted_flag = bytes.fromhex(encrypted_flag_hex)

# Mật khẩu (FLAG)
phrase = os.environ.get('FLAG', 'missing')

# Giải mã thông điệp
decrypted_flag = decrypt(phrase, encrypted_flag)
print(decrypted_flag)

