"""
Một trong những ví dụ đầu tiên về mã hóa được Julius Caesar sử dụng. Ý tưởng mật mã
này rất đơn giản: Mỗi chữ cái trong tin nhắn gốc được dịch chuyển 3 vị trí, tức là A chuyển thành
D, B chuyển thành E, C chuyển thành F, D chuyển thành G, v.v. Tương tự, 03 chữ cái cuối cùng
trong bảng chữ cái được thay thế: X chuyển thành A, Y chuyển thành B và Z chuyển thành C.
Các ký tự không phải chữ cái thì giữ nguyên.
"""
class Caesar:
    def __init__(self, plaintext, shift):
        self.plaintext = plaintext
        self.shift = shift
    def CaesarEncrypt(self):
        cipher = ""
        for char in self.plaintext:
            if char.isalpha():
                shift_amount = self.shift % 26
                if char.islower():
                    start = ord('a')
                else:
                    start = ord('A')
                char_code = ord(char) - start 
                new_char_code = (char_code + shift_amount ) %26
                new_char = chr(start + new_char_code)
                cipher += new_char
            else:
                 cipher += char
        return cipher
                
if __name__=="__main__":
    plaintext = str(input("Nhập messenger của bạn vào đây: "))
    shift = int(input("Nhập số hàng bạn muốn di chuyển: "))
    decrypt = Caesar(plaintext, shift)
    result = decrypt.CaesarEncrypt()
    print(f"Messager sau khi encrypt là: {result}")