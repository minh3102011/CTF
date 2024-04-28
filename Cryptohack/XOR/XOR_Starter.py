
xor = ''.join([chr(ord(c) ^ 13) for c in 'label'])
#''.join để biến chuỗi string a, l, o, h, a thành aloha
#ord để biến giá trị c từ dạng kí tự thành dạng số ascii để xor với 13 và cho lặp kí tự c trong chuỗi string label
#sau khi xor ta được mã unicode dùng chr để chuyển từ unicode thành dạng chữ có thể đọc được
print(xor)
