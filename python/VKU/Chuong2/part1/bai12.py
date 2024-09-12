"""
Viết chương trình nhập chi phí của một bữa ăn tại nhà hàng từ người dùng. Chương
trình sẽ tính thuế và tiền boa cho bữa ăn. Trong đó, tiền boa là 18% số tiền bữa ăn (không có
thuế); tiền thuế là 5% số tiền bữa ăn. Đầu ra của chương trình là tổng tiền, gồm: thuế, số tiền
boa và tiền bữa ăn. Định dạng đầu ra sao cho tất cả các giá trị được hiển thị bằng hai con số
thập phân
"""
meal_cost = float(input("Nhập chi phí của bữa ăn (VND): "))


tax = meal_cost * 0.05
tip = meal_cost * 0.18


total_cost = meal_cost + tax + tip

print(f"Tiền thuế: {tax:.2f} VND")
print(f"Tiền boa: {tip:.2f} VND")
print(f"Tổng số tiền phải trả: {total_cost:.2f} VND")
