import sys

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

chars = ""
from fileinput import input
for line in input("/home/bien/CTF/Picoctf/2024/ciphertext"):
  chars += line

decrypted_message = ""
prev = 0
for char in chars:
    cur = lookup2.index(char)
    decrypted_char_index = (cur + prev) % 40
    decrypted_message += lookup1[decrypted_char_index]
    prev = decrypted_char_index 

print(decrypted_message)
