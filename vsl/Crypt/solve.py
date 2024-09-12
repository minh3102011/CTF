
enc = "16520d02510c523e15513e17120d3e5351535416520d02510c523e1551"
plaint = 'a'*len(enc)
hex_bytes = bytes.fromhex(enc)
print(hex_bytes)
key_bytes = bytes.fromhex(plaint.encode().hex())
xor_result = bytes([b1 ^ b2 for b1, b2 in zip(hex_bytes, key_bytes)])
print(xor_result)
