#Viết chương trình tính diện tích tam giác theo công thức. Yêu cầu nhập vào 3 cạnh và các góc A,B và C (radian)
import math as m
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))
C = m.radians(float(input("Góc C: ")))
A = m.radians(float(input("Góc A: ")))
B = m.radians(float(input("Góc B: ")))
if (A+B+C!=180 ):
    print("khong hop le tong ba goc phai = 180")
else:
    print(f"S = 1/2*a*b*m.sin(C) = {1/2*a*b*m.sin(C)}")
    print(f"S = 1/2*b*c*m.sin(A) = {1/2*b*c*m.sin(A)}")
    print(f"S = 1/2*a*c*m.sin(B) = {1/2*a*c*m.sin(B)}")
