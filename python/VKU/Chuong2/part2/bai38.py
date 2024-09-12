def main():
    negative_numbers = []
    zero_numbers = []
    positive_numbers = []
    
    while True:
        user_input = input("Nhập số nguyên (hoặc nhấn Enter để kết thúc): ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            if number < 0:
                negative_numbers.append(number)
            elif number == 0:
                zero_numbers.append(number)
            else:
                positive_numbers.append(number)
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
    
    print("\nCác số đã nhập theo thứ tự yêu cầu:")
    for number in negative_numbers + zero_numbers + positive_numbers:
        print(number)

if __name__ == "__main__":
    main()
