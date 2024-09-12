"""
Một số nguyên, n, được cho là hoàn hảo khi tổng của tất cả các ước số của n bằng n. Ví
dụ, 28 là một số hoàn hảo vì các ước số của nó là 1, 2, 4, 7 và 14. Tổng 1 + 2 + 4 + 7 + 14 = 28.
Viết hàm xác định xem số nguyên dương có hoàn hảo hay không.
"""
class PerfectNumber:
    def __init__(self, num):
        self.num = num
    def ChecKNum(self):
        list = []
        total = 0
        for i in range(1, self.num//2+1):
            if self.num % i == 0:
                list.append(i)
        for i in range(len(list)):
            total =total + list[i]
        if total == self.num:
            return print(f"{total} = {self.num} => Perfect")
        else:
            return print(f'{total} != {self.num} => No Perfect')
if __name__=="__main__":
    num = int(input("Nhập vào số bạn muốn tính: "))
    perfect = PerfectNumber(num)
    result  = perfect.ChecKNum()

            