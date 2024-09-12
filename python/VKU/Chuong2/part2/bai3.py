"""
Viết một chương trình kiểm tra một chuỗi có trong chuỗi khác. Yêu cầu:

Nhập vào một chuỗi st

Nhập vào chuỗi cần tìm st_search

Nếu có thì in ra màn hình "Đã tìm thấy chuỗi cần tìm, tại vị trí: …”.
"""
st = input("Enter your string: ")

st_search = input(" Enter a searching string :")

if st_search in st:

    print(" A search string was found, at location :" +

str(st.find(st_search)))

else:

    print("Not Found")