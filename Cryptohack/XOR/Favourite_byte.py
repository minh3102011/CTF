input = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
flag = [chr(ord(i) ^ flag) for flag in 256 for i in input]
print(flag)
