"""
Một số được gọi là số Amstrong bậc N, nếu nó là số nguyên dương và tổng bậc N của các
các chữ số cấu thành thì bằng chính số đó.Ví dụ:

Số Amstrong bậc 4: abcd = a4 + b4 + c4 + d4

Số Amstrong bậc N: abc….d = aN + bN + cN + ….+ dN

Cụ thể: 153 = 1*1*1 + 5*5*5 + 3*3*3 nên 153 số Amstrong.

Viết chương trình nhập vào 1 số, cho biết số đó có phải là số Amstrong hay không?
"""
num = int(input("Enter a number: "))

level = int(input("Bậc: "))

sum = 0

temp = num

while temp > 0:

    digit = temp % 10

    sum += digit ** level

    temp //= 10

if num == sum:

    print(num, "is Amstrong, level : " + str(level))

else:

    print(num, "is not Amstrong")