m = float(input("Nhap khoi luong nuoc (g): "))
deltaT = float(input("Nhap su thay doi delta T (do Celsius): "))
Q = 4.186 * deltaT * m 
print(f'Q = M * C * deltaT = {Q}')
print(f'chi phi = {Q*2.777e-7*0.089}')