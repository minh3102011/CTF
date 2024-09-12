"""
Viết một hàm có một tham số password để xác định xem mật khẩu có tốt hay không. Một
mật khẩu tốt là một mật khẩu dài ít nhất 8 ký tự và chứa ít nhất một chữ cái viết hoa, ít nhất một
chữ cái viết thường và ít nhất một số. Hàm sẽ trả về True nếu mật khẩu là tốt, ngược thì nó sẽ trả
về Fales. Chương trình có một chương trình chính đọc mật khẩu từ người dùng và hiển thị xem nó
có tốt hay không.
"""
class PasswordCheck:
    def __init__(self, str1):
        self.str1 = str1
    def Check(self):
        if len(self.str1) < 8:
            return False
        if any(char.isupper()for char in self.str1) and any(char.islower() for char in self.str1) and any(char.isdigit() for char in self.str1):
            return True
        else:
            return False
if __name__ == "__main__":
    passwd = str(input("Nhập pass vào dây: "))
    check = PasswordCheck(passwd)
    result = check.Check()
    
    if result:
        print(f"{passwd} là mật khẩu xịn ")
    else:
        print(f"{passwd} không phải là mật khẩu xịn")
