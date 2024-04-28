chars = ""
from fileinput import input
for line in input("/home/bien/CTF/Picoctf/2024/ciphertext"):
    chars += line
b = 1

for i in range(len(chars)):
    if i == (b * b * b):
        print(chars[i], end="")
        b += 1

print()
