"""
Viết hàm không có tham số để tạo mật khẩu ngẫu nhiên. Mật khẩu phải có độ dài ngẫu
nhiên từ 7 đến 10 ký tự. Mỗi ký tự phải được chọn ngẫu nhiên từ các vị trí 33 đến 126 trong bảng
ASCII. Hàm sẽ trả về mật khẩu được tạo ngẫu nhiên. Hiển thị mật khẩu được tạo ngẫu nhiên trong
chương trình chính.
"""
import random
class RandomPassword:
    def __init__(self):
        self.list = []
    def PassRan(self):
        ran = random.randint(7,10)
        for i in range(ran):
            random_num = random.randint(33,126)
            self.list.append(chr(random_num))
        return self.list
if __name__ == "__main__":
    ran = RandomPassword()
    print(''.join(ran.PassRan()))
        