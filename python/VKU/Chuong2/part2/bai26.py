class CharacterChecker:
    def __init__(self, char):
        self.char = char.lower()

    def check_character(self):
        if self.char in 'aeiou':
            return f"Chữ cái '{self.char}' là nguyên âm."
        elif self.char == 'y':
            return "Chữ cái 'y' có thể là nguyên âm hoặc phụ âm."
        else:
            return f"Chữ cái '{self.char}' là phụ âm."

if __name__ == "__main__":
    char = input("Nhập một chữ cái: ")
    checker = CharacterChecker(char)
    result = checker.check_character()
    print(result)
