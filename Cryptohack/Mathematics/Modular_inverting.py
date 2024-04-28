from Crypto.Util.number import *
d = inverse(3,13)
print(d)
'''
pow(3,13-2,13)
3*d = 1 mod 13
d = 3^(13-2) mod 13
a^(p-1) ≡ 1 mod p <=> a^(p-1) % p = 1

a^(p-1) ≡ 1 mod p
a^(p-1) * a^(-1) ≡ a^(-1) mod p
a^(p-2) * a * a^(-1) ≡ a^(-1) mod p
a^(p-2) ≡ a^(-1) mod p 
<=>
a^(p-2) % p = a^(-1)

3 * d ≡ 1 mod 13
# Which can be written
3^(13-2) % 13 = 9
'''
