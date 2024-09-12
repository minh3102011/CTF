"""
Với số nguyên n nhất định, hãy viết chương trình tạo ra một dictionary chứa (i, i*i) với i là
số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này. Ví dụ: Giả sử số n là 8 thì
đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
"""
class SquareDict:
    def __init__(self, n):
        self.n = n
        self.square_dict = {}

    def generate_dict(self):
        self.square_dict = {i: i*i for i in range(1, self.n + 1)}

    def display_dict(self):
        print("Dictionary chứa các cặp (i, i*i):")
        print(self.square_dict)


    

if __name__ == "__main__":
    n = int(input("Nhập số nguyên n: "))
    square_dict = SquareDict(n)
    square_dict.generate_dict()
    square_dict.display_dict()

    