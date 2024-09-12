"""
Viết chương trình loại bỏ các ký tự không phải là ký tự CHỮ CÁI và SỐ trong một chuỗi.

Ví dụ: Từ st1 = "He is very handsome@%^&%^"

Trích thành chuỗi st2 = "He is very handsome“
"""
# Định nghĩa chuỗi các ký tự cần loại bỏ

st1 = """!()-[]{};:""\,<>./?@#$%^&*_~"""

my_str = "Hello!!!, he said ---and went."

# Nếu muốn người dung nhập chuỗi vào thì dung lệnh sau

# my_str = input(“Enter a string: ")

# Loại bỏ ký tự cần loại bỏ

st2 = ""

for char in my_str:

    if char not in st1:

        st2 = st2 + char

# Hiển thị chuỗi sau khi loại bỏ

print(st2)