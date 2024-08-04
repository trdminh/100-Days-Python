'''
So nguyen to
'''
from math import sqrt
n = int(input('Nhap gia tri: '))

check = True
for i in range(2,int(sqrt(n))+1):
    if n%i == 0:
        check = False
        break
print(check)