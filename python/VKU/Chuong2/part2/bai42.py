"""
Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in
thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra
phải là 40320. Yêu cầu: định nghĩa hàm tính giai thừa
"""
class Factorial:
    def __init__(self, num) :
        self.num = num
    def Factorial_Calculator(self):
        result=1
        for i in range(1, self.num+1):
            result*=i
        return result
if __name__ == "__main__":
    num = int(input("Nhập vào số nguyên dương: "))
    factorial = Factorial(num)
    result = factorial.Factorial_Calculator()
    print(result)