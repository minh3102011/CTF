


def ave(a,b,c):
    return (a+b+c)/3

print(ave(1,3,2))

ave = lambda a, b, c: (a+b+c)/3

print(ave(1,3,2))
x_power_a = lambda x, a=2 : x ** a
print(x_power_a(2)) # 2**2
print(x_power_a(2,5)) # 2**5

def kteam():
    mem = lambda x: x+ ' is a member of Kteam'
    return mem # trả về một hàm ẩn danh
call_mem = kteam() # lấy biến call_mem giữ hàm ẩn danh
print(call_mem('Bien')) # giá trị chuỗi được đưa vào biến x

