import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password = []
random_letter = random.randint(0, 51)
random_number = random.randint(0,9)
random_symbol = random.randint(0,8)
for i in range(nr_letters):
    random_letter = random.randint(0, 52)
    password.append(letters[random_letter])
for i in range(nr_symbols):
    random_symbol = random.randint(0,8)
    password.append(symbols[random_symbol])
for i in range(nr_numbers):
    random_number = random.randint(0,9)
    password.append(numbers[random_number])
random.shuffle(password)
print(f"Pass: {''.join(password)}")
