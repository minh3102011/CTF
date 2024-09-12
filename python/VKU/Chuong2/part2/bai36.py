"""
Viết chương trình đọc các số nguyên từ người dùng và lưu trữ chúng trong danh sách.
Chương trình sẽ tiếp tục đọc các giá trị cho đến khi người dùng nhập ký tự 0. Sau đó, nó sẽ hiển
thị tất cả các giá trị được nhập bởi người dùng (ngoại trừ 0) theo thứ tự tăng dần, với một giá trị
xuất hiện trên mỗi dòng. Sử dụng phương thức sắp xếp hoặc hàm được sắp xếp để sắp xếp danh
sách.
"""
class Storage:
    def __init__(self):
        self.numbers = []
    def AddNumber(self, num):
        if num !=0:
            self.numbers.append(num)
    def SortNum(self):
        self.numbers.sort()
    def DisplayResult(self):
        print("Các số đã nhập theo thứ tự tăng dần là: ")
        for num in self.numbers:
            print(num, end=', ')
if __name__=="__main__":
    num_List= Storage()
    while True:
        try:
            num = int(input("Nhập số bạn muốn sắp xếp vào dây: "))
            if num ==0:
                break
            num_List.AddNumber(num)
            num_List.SortNum()
          
        except ValueError:
            print("Kí tự bạn nhập không phải số nguyên")
    num_List.DisplayResult()