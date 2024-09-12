"""
Viết một chương trình tìm tất cả các số trong đoạn 100 và 300 (tính cả 2 số này) sao cho tất
cả các chữ số trong số đó là số chẵn. In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên
một dòng.
"""
values = []
for i in range(100, 301):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) :
        values.append(s)
print(",".join(values))