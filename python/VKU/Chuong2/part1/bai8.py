#Viết chương trình tính diện tích tam giác đều theo định lý Heron. Yêu cầu nhập vào cạnh tam giác đều.
import math as m
a = float(input("nhap canh a: "))
print(f"S = a^2 * sprt(3)/4 = {m.pow(a,2)* m.sqrt(3)/4}")