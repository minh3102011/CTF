"""
Nhập vào một chuỗi

Nhập vào một từ cần thay thế và một từ thay thế.

Sau đó, hiển thị kết quả ra màn hình.
"""
st1 = input("Enter your string: ")

st2 = input(" Enter the word that needs to replace: ")
st3 = input(" Enter the word after being replaced: ")

st1 = st1.replace(st2,st3)

print(st1)
