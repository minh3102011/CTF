# viết chương trình tính 1/2+2/3+3/4+...+n/(n+1) với n là số nguyên dương nhập vào n> 0
n=int(input(" Enter an integer greater than 0 : "))

sum=0.0

for i in range(1,n+1):

    sum += float(float(i)/(i+1))

print(sum)