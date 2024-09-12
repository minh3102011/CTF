"""
Định nghĩa một hàm có thể tạo danh sách chứa các giá trị bình phương của các số từ 1
đến 20 (bao gồm cả 1 và 20) và in 5 phần tử đầu tiên trong danh sách. Yêu cầu: Sử dụng toán tử
** để lấy giá trị bình phương; Sử dụng range() cho vòng lặp; Sử dụng list.append() để thêm phần
tử vào danh sách; Sử dụng [n1:n2] để cắt danh sách.
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
    list = square.Cal_square()
    list_first = list[1:len(list)//2+1]
 
    list_sec  = list[len(list)//2+1:len(list)]
  
    print(list_first)
    print(list_sec)