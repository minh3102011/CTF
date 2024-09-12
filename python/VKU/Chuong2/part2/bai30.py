"""
Hầu hết các năm có 365 ngày. Tuy nhiên, thời gian cần thiết để Trái đất quay quanh Mặt trời
thực sự nhiều hơn thế một chút. Do đó, thêm một ngày, ngày 29 tháng 2, được đưa vào một số năm
để khắc phục sự khác biệt này. Những năm như vậy được gọi là năm nhuận. Các quy tắc để xác
định xem một năm có phải là năm nhuận hay không:

Bất kỳ năm nào chia hết cho 400 là một năm nhuận.

Trong số các năm còn lại, bất kỳ năm nào chia hết cho 100 không phải là năm nhuận.

Trong số các năm còn lại, bất kỳ năm nào chia hết cho 4 là một năm nhuận.

Tất cả các năm khác không phải là năm nhuận.

Viết chương trình đọc một năm từ người dùng và hiển thị thông báo cho biết đó có phải là năm nhuận hay
không
"""
class Year:
    def __init__(self, year):
        self.year = year
    def LeapYear(self):
        if self.year % 400 == 0:
            return True
        else:
            if self.year % 100 == 0:
                return False
            elif self.year % 4 ==0:
                return True
            else:
                return False
if __name__ == "__main__":
    year = int(input("Nhập năm bạn muốn vào đây: "))
    leapYear = Year(year)
    result = leapYear.LeapYear()
    if result:
        print(f"Năm {year} là năm nhuận")
    else:
        print(f'Năm {year} là năm không nhuận')