encrypt_text = '4C6520666C6167206465206365206368616C6C656E6765206573743A203261633337363438316165353436636436383964356239313237356433323465'
decrypt_text = bytes.fromhex(encrypt_text).decode("ASCII")
print(decrypt_text)
#another solution

import binascii
p = binascii.unhexlify(encrypt_text)
print(p.decode('ASCII'))

