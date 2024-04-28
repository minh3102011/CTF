from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import *
r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])
    
encoding = received["type"]
word = received["encoded"]
def decode(t, data):
    if t=='base64':
        return base64.b64decode(data).decode()
    elif t=='hex':
        return binascii.unhexlify(data).decode()
    elif t=='bigint':
        return long_to_bytes(int(data,16)).decode()
    elif t== 'rot13':
        return codecs.decode(data, 'rot13')
    elif t== 'utf-8':
        s= ""
        for c in data:
            s += chr(c)
        return s

while True:
    received = json_recv()
    if 'flag' in received:
        print(received['flag'])
        sys.exit(0)
    to_send = {
        "decoded": decode(encoding, word)
    }

    json_send(to_send)

    json_recv()
