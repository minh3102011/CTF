"""
Viết hàm có 03 tham số và trả về giá trị trung bình của các tham số đó. Bao gồm một
chương trình chính đọc ba giá trị từ người dùng và hiển thị giá trị trung bình của chúng.
"""
class Average:
    def __init__(self, num1, num2, num3) :
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def Cal_Average(self):
        return print(f"Giá trị trung bình là {(self.num3 + self.num2 + self.num1)/3}")
if __name__=="__main__":
    num1 = float(input("Nhập số thứ nhất: "))
    num2 = float(input("Nhập số thứ hai: "))
    num3 = float(input("Nhập số thứ ba: "))
    ave = Average(num1, num2, num3)
    result = ave.Cal_Average()