
The value received from Alice is the following value
A = g^a mod p
powering this by b, you get
key = A^b mod p
    = g^(a*b) mod p
    
This is the secret value to share.

-----------------------------------------------------------
Alice will calculate the value you sent in the same way
and get the same value.
B = g^b mod p
key = B^a mod p
    = g^(a*b) mod p
    
    
-----------------------------------------------------------
-----------------------------------------------------------
The value p, g, A, B are safe for the hacker to know, 
but a and b must not be known.
