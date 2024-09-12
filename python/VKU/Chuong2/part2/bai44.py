"""
Định nghĩa một hàm có thể tạo và in danh sách chứa các giá trị bình phương của các số
từ 1 đến 20 (tính cả 1 và 20). Yêu cầu: Sử dụng toán tử ** để lấy giá trị bình phương; Sử dụng
range() cho vòng lặp; Sử dụng list.append() để thêm giá trị vào danh sách.
"""
class Cal_Square:
    def __init__(self) :
        self.list = []
    def Cal_square(self):
        for i in range(0, 21):
            self.list.append(i**2)
        return self.list
       
if __name__=="__main__":
    square= Cal_Square()
    print(square.Cal_square())
   