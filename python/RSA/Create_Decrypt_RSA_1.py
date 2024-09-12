from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.hashes import SHA256

#create private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024
)
p = private_key.private_numbers().p
q = private_key.private_numbers().q
print(f"p: {p}")
print(f"q: {q}")

#create public key
public_key = private_key.public_key()
n = public_key.public_numbers().n
e= public_key.public_numbers().e
print(f"n: {n}")
print(f"e: {e}")


#encrypt with public key
plaintext= b'dokki'

oaep_padding = padding.OAEP(mgf=padding.MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
ciphertext = public_key.encrypt(plaintext, oaep_padding)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")

#decrypt with private key
recovered_plaintext = private_key.decrypt(ciphertext, oaep_padding)
assert( recovered_plaintext == plaintext )
print(f'recovered_plaintext: {recovered_plaintext}')
#Verify that 190 bytes can be encrypted
plaintet = b'\xff' *190
public_key.encrypt(plaintext,oaep_padding)

#Veryfy that 191 bytes can't be encrypted
try:
    plaintet = b'\xff' *190
    public_key.encrypt(plaintext,oaep_padding)
except ValueError:
    pass
else:
    assert False
