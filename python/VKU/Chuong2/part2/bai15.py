"""
Viết chương trình nhập một chuỗi số, phân tách bằng dấu phẩy. In ra một danh sách và một
tuple chứa mọi số.

Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:

["34", "67", "55", "33", "12", "98"]
("34", "67", "55", "33", "12", "98")
"""
chuoi=input("Nhập vào các giá trị:")
kieu_ds=chuoi.split(",")
kieu_tuples=tuple(kieu_ds)
print(kieu_ds)
print(kieu_tuples)