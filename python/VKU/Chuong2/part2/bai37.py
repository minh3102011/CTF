def main():
    words = []
    unique_words = set()
    
    while True:
        word = input("Nhập từ (hoặc nhấn Enter để kết thúc): ")
        if word == "":
            break
        if word not in unique_words:
            words.append(word)
            unique_words.add(word)
    
    print("\nCác từ đã nhập (không trùng lặp):")
    for word in words:
        print(word)

if __name__ == "__main__":
    main()
