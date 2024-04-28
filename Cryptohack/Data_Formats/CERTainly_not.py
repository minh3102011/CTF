from Crypto.PublicKey import RSA
import OpenSSL.crypto
with open("/home/bien/Downloads/2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der", 'rb') as f:
    der = f.read()

x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, der)
pkey = x509.get_pubkey()
dir(pkey)
print(pkey.bits())
print(pkey.type() == OpenSSL.crypto.TYPE_RSA)

flag = RSA.import_key(der)
print(flag.n)

