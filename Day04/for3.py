n = int(input('Nhap n: '))
result = 1;
for i in range(1,n+1):
    result *= i

print('%d! = %d' % (n, result))