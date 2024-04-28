a = [1, 2, 3]
print(a)
a.append([4,5]) # thêm list vào list a output = [1,2,3, [4,5]]
a.extend([4,5]) # thêm phần tử 4 5 vào list a ouput = [1,2,3,4,5]
a.insert(1, 2) # chèn phần tử 2 vào vị trí thứ 1 output = [1 , 2 , 2 , 3]
b = a.pop() # đếm số phần tử trong list
a.reverse() # đảo ngược list a
a.sort() # sắp xếp theo thứ tự tăng dần
