"""
Viết một chương trình chấp nhận đầu vào là một câu, đếm số ký tự hoa, số ký tự
thường. Giả sử đầu vào là: Quản Trị Mạng

Thì đầu ra là: Chữ hoa: 3

Chữ thường: 8
"""
st = input(“Enter your sentence: ")

Sum_upper_Char = 0

Sum_lower_Char = 0

for c in st:

    if c.isupper():

        Sum_upper_Char +=1

    elif c.islower():

        Sum_lower_Char +=1

    else:

        pass

print(“Sum of Upper Character:", Sum_upper_Char)

print(“Sum of Lower Character:", Sum_lower_Char)