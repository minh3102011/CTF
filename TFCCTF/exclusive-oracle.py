def xor(first, second):
    length = max(len(second), len(first))
    data = b''
    i, j = 0, 0
    for _ in range(length):
        data += (first[i] ^ second[j]).to_bytes(1, 'big')
        i += 1
        j += 1
        i %= len(first)
        j %= len(second)
        if i == 0 or j == 0:
            return data
    return data
def count(a):
    count = 0
    for i in a:
        if i == '\\':
            count +=1
    return count
print(count(r"\xb5\x8c\xf8T\x8d\x91G\x00Mr\xfaG\xeb'\xf5\xfe\xd6o\xb4\x05V\xaa\xbf\xd83,c\xdf\x84\x9c\xa1~\x9a\x88\x98\xb9c\xe2\x81\xb5\x8c\xf8T\x8d\x91"))
enc = r"\xb5\x8c\xf8T\x8d\x91G"
key = [-1 for i in range(16)]
flag_st = "TFCCTF{"
for i in range(len(flag_st)):
    key[i] = ord(flag_st[i])^int(enc[i*2:(i+1)*2],len(enc))

print(key)



