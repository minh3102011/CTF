from pwn import xor
from Crypto.Util.number import *
#KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
#KEY2_KEY1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
#KEY2_KEY3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
#FLAG_KEY1_KEY3_KEY2 =bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
#print(KEY1)
#flag = xor(KEY2_KEY3, FLAG_KEY1_KEY3_KEY2,KEY1)
#print(flag)
key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
key2_key1 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
key3_key2 =  0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
flag = key1 ^ key3_key2 ^ 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
print(long_to_bytes(flag).decode())

