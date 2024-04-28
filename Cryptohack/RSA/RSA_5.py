from Crypto.Util.number import *
p = 857504083339712752489993810777

q = 1029224947942998075080348647219
e = 65537
# d *e = 1 mod phi
# phi =(q-1)*(p-1)
phi = (q-1)*(p-1)
d = inverse(e, phi)
print(d)
