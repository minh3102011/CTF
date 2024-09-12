import string
from base64 import b64decode
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'

def reverse_generate_password(password):
    master_key = 0
    for char in reversed(password):
        master_key <<= 1
        if char in ALPHABET[:len(ALPHABET)//2]:
            master_key |= 1
        elif char in ALPHABET[len(ALPHABET)//2:]:
            master_key |= 0
        else:
            raise ValueError("Invalid character in password")
    return master_key

password = "jfeTBdx!Dq0Uay$TUOpr&aaKCFV$3yuU~M63zv66v9id5nFRxcYYow" 

master_key = reverse_generate_password(password)
master_key_bytes = master_key.to_bytes((master_key.bit_length() + 7) // 8, byteorder='little')

print("Master Key:", master_key)
print("Master Key Bytes:", master_key_bytes)
ciphertext_b64 = "rD0qyT/JPCQI2tZWx6pRyx3O7782Fpm6a7yPKtm6dLE="
ciphertext = b64decode(ciphertext_b64)

# Tạo khóa giải mã từ master key
encryption_key = sha256(master_key_bytes).digest()

# Giải mã ciphertext
cipher = AES.new(encryption_key, AES.MODE_ECB)
decrypted_data = unpad(cipher.decrypt(ciphertext), 16)

print("Decrypted Message:", decrypted_data.decode())
