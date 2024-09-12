"""
Định nghĩa một hàm có đầu vào là 2 chuỗi và in chuỗi có độ dài lớn hơn. Nếu 2 chuỗi có
chiều dài như nhau thì in tất cả các chuỗi theo dòng. Sử dụng hàm len() để lấy chiều dài của một
chuỗi.
"""
class Length_String:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
    def Cal_Length(self):
        if(len(self.string1) > len(self.string2)):
            return print(f'{self.string1} dài hơn')
        elif(len(self.string1) < len(self.string2)):
            return print(f'{self.string2} dài hơn')
        else:
            return print(f'{self.string1}\n{self.string2}')
        
if __name__=="__main__":
    str1 = str(input("Nhập chuỗi 1: "))
    str2 = str(input("Nhập chuỗi 2: "))
    lenstr = Length_String(str1, str2)
    result = lenstr.Cal_Length()
  