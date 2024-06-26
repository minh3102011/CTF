from cryptography.hazmat.primitives import  padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asymmetric_padding
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
import os

def hybrid_decrypt(plaintext, public_key, private_key):
    # Decrypt AES key
    oaep_padding = asymmetric_padding.OAEP(mgf=asymmetric_padding.MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
    recovered_key = private_key.decrypt(cipherkey, oaep_padding)

    # Decrypt padded plaintext
    aes_cbc_cipher = Cipher(AES(recovered_key), CBC(ciphertext['iv']))
    recovered_padded_plaintext = aes_cbc_cipher.decryptor().update(ciphertext['ciphertext'])

    # Remove padding
    pkcs7_unpadder = padding.PKCS7(AES.block_size).unpadder()
    recovered_plaintext = pkcs7_unpadder.update(recovered_padded_plaintext) + pkcs7_unpadder.finalize()

    return recovered_plaintext 
    

def hybrid_encrypt(plaintext , public_key):
    #Pad the Plaintext
    pkcs7_padder = padding.PKCS7(AES.block_size).padder()
    padded_plaintext = pkcs7_padder.update(plaintext)+ pkcs7_padder.finalize()

    #Generate new random AES-256 key
    key = os.urandom(256 //8)

    # Generate new random 128-bit IV
    iv = os.urandom(128 // 8)

    #AES CBC cipher
    aes_cbc_cipher = Cipher(AES(key), CBC(iv))
    #Encrypt padded Plaintext
    ciphertext = aes_cbc_cipher.encryptor().update(padded_plaintext)
    
    #Encrypt AES key
    oaep_padding = asymmetric_padding.OAEP(mgf=asymmetric_padding.MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
    cipherkey = public_key.encrypt(key, oaep_padding)

    return {'iv': iv, 'ciphertext': ciphertext}, cipherkey

# Recipient's private key
private_key = rsa.generate_private_key(
    public_exponent= 65537,
    key_size= 2048
)

# Public key to make availble to senders
public_key = private_key.public_key()

# Plaintext to hybrid encrypt
plaintext = b'Fundamental Cryptography in Python'

# Hybrid encrypt Plaintext
ciphertext, cipherkey = hybrid_encrypt(plaintext, public_key)

# Hybrid decrypt plaintext 
recovered_plaintext = hybrid_decrypt(ciphertext, cipherkey, private_key)

assert(recovered_plaintext == plaintext)

print(recovered_plaintext)
print(ciphertext)
print(cipherkey)
