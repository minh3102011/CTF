"""
Viết một chương trình tạo ra một danh sách các số lẻ từ các số được người dùng nhập
vào. Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
"""
class Odd:
    def __init__(self, num):
        self.num = num
    def OddCheck(self):
        return [so for so in self.num if so % 2 != 0]
        
if __name__ == "__main__":
    listNum = input('Nhập list số cách nhau bởi dấu , : ')
    list = [int(so) for so in listNum.split(",")]
    listOdd = Odd(list)
    result = listOdd.OddCheck()
    print(result)