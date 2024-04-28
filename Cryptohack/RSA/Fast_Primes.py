from Crypto.PublicKey import RSA
from Crypto.Util.number import *
c = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28
f = open('/home/bien/Downloads/key_17a08b7040db46308f8b9a19894f9f95.pem','r')
key = RSA.import_key(f.read())
print(key.n)
e = 65537

