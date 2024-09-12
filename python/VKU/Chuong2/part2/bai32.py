"""
Mở rộng viết chương trình mã hóa mã Caesar, cho phép người dùng cung cấp tin nhắn
và sau đó hiển thị tin nhắn đã được mã hóa. Chương trình cũng hỗ trợ giải mã (chuyển ngược
lại) để có thể sử dụng cả hai chức năng: mã hóa tin nhắn và giải mã tin nhắn. Và số ký tự dịch
chuyển do người dùng nhập.
"""
from bai31 import *
def Decrypt(cipher, shift):
    caesar = Caesar(cipher, -shift)
    result = caesar.CaesarEncrypt()
    return result
if __name__ == "__main__":
    plaintext = str(input("Nhập vào đây messenger của bạn: "))
    shift = int(input("Nhập vào đây số hàng bạn muốn dịch chuyển: "))
    caesar = Caesar(plaintext, shift)
    cipher = caesar.CaesarEncrypt()
    print(f"Messenge của bạn sau khi mã hóa là {cipher}")
    decrypt = Decrypt(cipher, shift)
    print(f"Plaintext là: {decrypt}")