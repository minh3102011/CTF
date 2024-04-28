from Crypto.Util.number import long_to_bytes
from sympy import gcd
from gmpy2 import *
# Đọc các giá trị từ tệp public-key.txt
with open('public-key.txt', 'r') as f:
    lines = f.readlines()
    n1 = int(lines[0].split(': ')[1])
    n2 = int(lines[1].split(': ')[1])
    n3 = int(lines[2].split(': ')[1])
    e = int(lines[3].split(': ')[1])
    c = int(lines[4].split(': ')[1])

def decrypt2(c,p,q,e):
    ph=(q-1)*(p-1) #tìm phi
    d = invert(e,ph) #tìm d theo công thức (d*e)%p(n) = 1
    return pow(c,d,q*p) # trả về kết quả tính của c^d modulo N

# Tìm p, q, r
p = gcd(n1, n2) # vì n1=p*q, n2=p*r trong n1 có nhân với p nên hàm gcd sẽ trả về giá trị p
q = n1 // p # vì n1 = p*q nên q = n1 // p 
r = n2 // p
a1 = decrypt2(c,q,r,e) #decryp RSA lần 1 vì trong encode gốc phép tính cuối cùng là pow(c,e,n3) mà n3 = q*r nên khi decrypt sẽ làm từ cuối
a2 = decrypt2(a1, p,r,e) #decrypt RSA lần 2
a3= decrypt2(a2,q,p,e) # decrypt RSA lần 3

# Chuyển đổi thông điệp từ số nguyên sang hex bằng format(a3,'x') và chuyển hex thành bytes bằng bytes.fromhex() và decode thành mã ascii
text = bytes.fromhex(format(a3,'x')).decode('ascii')
print(text)

"""
from gmpy2 import *

def decrypt(c, p, q, e):
     ph = (p-1)*(q-1)
     d = invert(e, ph) #( d * e ) % p( n ) = 1 and calculate d
     return pow(c, d, p*q)

params = {}
with open("/home/bien/Downloads/public-key.txt") as f:
    for line in f:
        line = line.rstrip()
        name, value = line.split(":")
        params[name] = mpz(int(value))

p = gcd(params["n1"], params["n2"])
q = gcd(params["n1"], params["n3"])
r = gcd(params["n2"], params["n3"])

assert(p * q == params["n1"])
assert(p * r == params["n2"])
assert(q * r == params["n3"])

a1 = decrypt(params["c"], q, r, params["e"])
a2 = decrypt(a1, p, r, params["e"])
a3 = decrypt(a2, p, q, params["e"])

print(bytes.fromhex(format(a3, 'x')))
"""

