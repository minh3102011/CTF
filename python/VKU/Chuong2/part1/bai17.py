"""
Khi gió thổi trong thời tiết lạnh, làm cho không khí lạnh hơn so với thực tế. Nguyên nhân
là do sự chuyển động của không khí làm tăng tốc độ làm mát cho các vật thể (chẳng hạn, như
con người).

Năm 2001, Canada, Vương quốc Anh và Hoa Kỳ đã áp dụng công thức sau đây để tính toán chỉ số
gió lạnh: WCI = 13,12 + 0,6215Ta - 11,37V0.16 + 0,3965Ta V0.16

Trong công thức Ta là nhiệt độ không khí tính bằng độ C và V là tốc độ gió tính bằng km/giờ.

Viết chương trình đọc nhiệt độ không khí và tốc độ gió từ người dùng. Hiển thị chỉ số gió lạnh được
làm tròn đến số nguyên gần nhất.


def calculate_wci(t, wind_speed):
    wci = 13.12 + 0.6215 * t - 11.37 * wind_speed**0.16 + 0.3965 * t * wind_speed**0.16
    return round(wci)

temperature = float(input("Nhập nhiệt độ không khí (°C): "))
wind_speed = float(input("Nhập tốc độ gió (km/h): "))

wci = calculate_wci(temperature, wind_speed)

print(f"Chỉ số gió lạnh là: {wci}")
"""
name = input("Nhap ten:")
print(f'Ten toi la {name} ')
