"""

Số ngày của một tháng thay đổi từ 28 đến 31 ngày. Viết một chương trình đọc tên của một
tháng từ người dùng dưới dạng một chuỗi. Sau đó, chương trình sẽ hiển thị số ngày trong tháng đó
(Chú ý: Số ngày là 28 hoặc 29 ngày để biểu diễn cho tháng 2).
"""
class Date:
    def __init__(self, date):
        self.date= date
    def dateInMonth(self):
        date = {
            1: "31 ngày",
            2: "28 ngày hoặc 29 ngày",
            3: "31 ngày",
            4: "30 ngày",
            5: "31 ngày",
            6: "30 ngày",
            7: "31 ngày",
            8: "31 ngày",
            9: "30 ngày",
            10: "31 ngày",
            11: "30 ngày",
            12: "31 ngày"            
        }
        if self.date in date:
            return f'Số ngày của tháng {self.date} là {date[self.date]}'
        else:
            return 'Tháng không hợp lệ'
if __name__=='__main__':
    try:
        date = int(input("Nhập tháng mà bạn muốn xem ngày: "))
        dateInMonth= Date(date)
        result = dateInMonth.dateInMonth()
        print(result)
    except ValueError:
        print("Vui lòng nhập tháng thích hợp")
        