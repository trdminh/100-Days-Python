n = int(input('Nhap gia tri n: '))

a = 0
b = 1
print(a,end=' ')
for i in range(n-1):
    a, b = b, a+b
    print('%d'%a,end=' ')

print()