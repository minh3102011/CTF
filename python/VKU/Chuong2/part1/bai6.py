"""
    Viết chương trình tính thể tích hình trụ V = πr2h với r là bán kính
của mặt đáy, h là chiều cao của hình trụ, và π là hằng số pi. Với r và h
nhập vào từ bàn phím.
"""
r = float(input("Enter r: "))
h = float(input("Enter h: "))
PI= float(3.14)
print(f"V = {r*r*h*PI}")