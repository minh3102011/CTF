class Palindrom:
    def __init__(self, text):
        self.text = text
    def palindromText(self):
        st = self.text.replace(" ","").lower()
        return text == self.text[::-1]
if __name__ == "__main__":
    text = str(input("Nhập chuỗi bạn muốn kiểm tra: "))
    palindrom = Palindrom(text)
    result = palindrom.palindromText()
    if result:
        print(f"Chuỗi là Palindrom")
    else:
        print(f"Chuỗi không phải là Palindrom")
    