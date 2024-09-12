"""
Viết chương trình đọc chiều dài và chiều rộng của một cánh đồng từ người dùng. Hiển thị
diện tích của cánh đồng theo theo đơn vị tính là Mẫu Anh. Gợi ý: Một Mẫu Anh bằng 43.560 met
vuông.
"""
width = float(input("Chieu dai (m): "))
length = float(input("Chieu rong (m): "))
print(f"S = width * length= {(width * length)/43.56 }")