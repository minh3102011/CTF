"""
Một hình tam giác có thể được phân loại dựa trên độ dài của các cạnh của nó. Tất cả ba
cạnh của một tam giác đều có cùng độ dài. Một tam giác cân có hai cạnh có cùng độ dài và một
cạnh thứ ba có độ dài khác nhau,... Viết chương trình đọc độ dài ba cạnh của một tam giác từ người
dùng. Sau đó hiển thị một thông báo cho biết loại tam giác.
"""
class Triangle:
    def __init__(self, triangle1, triangle2, triangle3):
        self.triangle1 = triangle1
        self.triangle2 = triangle2
        self.triangle3 = triangle3
    def triangleType(self):
        if self.triangle1 == self.triangle2:
            if self.triangle3 != self.triangle1:
                return print("Đây là tam giác cân")
            if self.triangle3 == self.triangle1:
                return print("Đây là tam giác đều")
        elif self.triangle1 **2 + self.triangle3**2 == self.triangle2**2 or self.triangle1**2 + self.triangle2**2== self.triangle3**2 or self.triangle3**2+ self.triangle2**2 == self.triangle1**2:
            return print("đây là tam giác vuông")
        else:
            return print("Đây là tam giác thường")
        
if __name__=="__main__":
    triangle1 = float(input("Nhập vào cạnh thứ nhất: "))
    triangle2 = float(input("Nhập vào cạnh thứ hai: "))
    triangle3 = float(input("Nhập vào cạnh thứ ba: "))
    triangle = Triangle(triangle1, triangle2, triangle3)
    result = triangle.triangleType()
    