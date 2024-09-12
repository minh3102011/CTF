"""
Viết chương trình chuyển đổi số thập phân thành nhị phân. Đọc số thập phân từ người
dùng dưới dạng số nguyên. Hiển thị kết quả, cùng với một thông điệp thích hợp.
"""
class Binary:
    def __init__(self, dex):
        self.dex = dex
    def binaryConvert(self):
        if self.dex == 0:
            return "0"
        binary =""
        while self.dex > 0:
            binary= str(self.dex%2)+ binary
            self.dex //=2
        return binary
if __name__=="__main__":
    dex = int(input("Nhập số thập phân bạn muốn chuyển đổi: "))
    binary = Binary(dex)
    result = binary.binaryConvert()
    print(result)