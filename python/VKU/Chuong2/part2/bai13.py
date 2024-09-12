"""
13: Viết một chương trình cho phép người dung nhập vào một chuỗi trên nhiều dòng, sau đó
chuyển các dòng này thành chữ in hoa và in ra màn hình. Yêu cầu:

Giả sử đầu vào là:

chào các bạn

thân mến

Đầu ra:

CHÀO CÁC BẠN

THÂN MẾN
"""

lines = []

while True:

    s = input()

    if s:

        lines.append(s.upper())

    else:

        break

for sentence in lines:

    print(sentence)