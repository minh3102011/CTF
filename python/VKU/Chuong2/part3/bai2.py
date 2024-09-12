try:

    with open('alice.txt') as f_obj: # Mở file và tạo biến đối tượng f_obj

        contents = f_obj.read() # Đọc và lưu nội dung file alice.txt

# vào biến contents

except FileNotFoundError: # Xử lý ngoại lệ không mở được file

    msg = "File " + filename + " không tồn tại."

    print(msg)

else: #Trường hợp đọc file hợp lệ

    words = contents.split() # Tách các từ trong biến contents lưu vào danh

# sách words

    num_words = len(words) # Đếm số từ lưu vào biến num_words

    print("File " + filename + " có" + str(num_words) + " từ.")