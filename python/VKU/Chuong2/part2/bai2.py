"""
Viết một chương trình kiểm tra một chuỗi nhập vào từ bàn phím: Chuỗi hoa; Chuỗi
thường; Chuỗi chứa ký tự hoa và ký tự thường.
"""
st = input("Enter your string: ")

if st.isupper():

    print("This is an upper string")

elif st.islower():

    print("This is an lower string")

else:

    print(" This string contains upper and lower characters ")