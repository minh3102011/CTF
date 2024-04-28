alphabet ="0abcdefghijklmnopqrstuvwxyz"
number = [16, 9, 6, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
decrypt = "".join([alphabet[i] for i in number])
print(decrypt)
