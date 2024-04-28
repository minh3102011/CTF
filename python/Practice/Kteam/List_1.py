# giới hạn bởi cặp ngoặc vuông []
# các phần tử cách nhau bởi dấu ,
# có khả năng chứa mọi giá trị và chứa chính nó
a = [i for i in range(30)]  #   tạo list a với biến i cho biến i chạy trong khoảng từ 0 tới 29
a = [[n,n*1,n*2] for n in range(1,4)]   # tạo list a với list n có công thức n, n*1, n*2 cho biến n chạy trong khoảng 1 -> 3
#constructor list
a= ['kteam'] # output = kteam
a = list('kteam') # output = 'k','t','e','a','m'
#a = list(1) # error list(interable) interable là một mảng hoặc 1 chuỗi hoặc 1 list tập hợp các phần tử int không phải là 1 interable
a = [1,2,[3,4]] # 1 chuỗi không cho phép nối nhưng list thì được a = 'bien' sẽ lỗi 
a+=['one','two'] # nối chuỗi
a *=2 # có thể nhân list với 1 số nhưng không thể nhân với 1 list
b = 1 in a # kiểm tra phần tử 1 có nằm trong list a không
b = a[2][0] # output = 3 lấy phần tử thứ 3 trong list và lấy phần tử thứ 1 trong list được lấy ra 
b = a[1:3] # lấy từ phần tử thứ 2 dến thứ 3 trong list
b = a[::-1] # đảo ngược list 
a[1] = 'bien' # đổi giá trị thứ 2 của list thành bien
a = [[1,2,3], [4,5,6]] # ma trận khi in ra theo dạng print(a[0])
print(a[0])
print(a)
print(b)
    # list có dạng 1 chiều còn ma trận có dạng 2 hoặc 3 chiều tương ứng với mảng 2 chiều
