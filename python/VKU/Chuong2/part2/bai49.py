"""
Số nguyên tố là một số nguyên lớn hơn 1 và chỉ chia hết cho 1 và chính nó. Viết hàm xác
định tham số của nó có phải là số nguyên tố hay không, trả về True nếu đúng và False nếu không
phải. Viết chương trình chính đọc số nguyên từ người dùng và hiển thị thông báo cho biết đó có
phải là số nguyên tố hay không.
"""
class Prime:
    def __init__(self, num):
        self.num = num
    def PrimeCheck(self):
        if self.num <= 1:
            return False
        for i in range(2, int(self.num**0.5) + 1):
            if self.num % i == 0:
                return False
        return True
if __name__ == "__main__":
    num = int(input("Nhập vào số bạn muốn kiểm tra: "))
    primeCheck = Prime(num)
    result = primeCheck.PrimeCheck()
    if result:
        print(f"{num} là số nguyên tố")
    else:
        print(f"{num} không phải là só nguyên tố")