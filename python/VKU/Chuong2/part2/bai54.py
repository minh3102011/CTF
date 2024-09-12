"""
Khi viết ra một danh sách các từ bằng tiếng Anh, người ta thường phân tách các từ bằng
dấu phẩy. Ngoài ra, thêm từ “and” trước từ cuối cùng, trừ khi danh sách chỉ chứa một từ. Hãy xem
xét bốn danh sách sau đây:

apples

apples and oranges

apples, oranges and bananas

apples, oranges, bananas and lemons

Viết hàm lấy danh sách các chuỗi làm tham số của nó. Hàm sẽ trả về một chuỗi chứa tất cả các từ
trong danh sách, được định dạng theo cách được mô tả như trên. Hàm hoạt động cho danh sách
có độ dài bất kỳ. Code bao gồm một chương trình chính đọc một số từ do người dùng nhập vào,
định dạng chúng bằng cách gọi hàm và sau đó hiển thị kết quả mà hàm trả về
"""

def format_list(words):
    if not words:
        return ""
    elif len(words) == 1:
        return words[0]
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]

def main():
    words = input("Nhập các từ, cách nhau bằng dấu phẩy: ").split(", ")
    formatted_string = format_list(words)
    print("Danh sách định dạng: " + formatted_string)

if __name__ == "__main__":
    main()
