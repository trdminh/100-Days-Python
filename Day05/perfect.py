'''

Số hoàn hảo là số có tổng các ước số của nó ngoại trừ chính nó bằng chính nó.
Ví dụ: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
'''

from math import sqrt

num = int(input('Nhap gia tri dau vao: '))

result = 0
for factor in range(1,int(sqrt(num))+1):
    if num%factor==0:
        result+=factor
        if factor > 1 and num//factor != factor:
            result += num//factor

if result == num:
    print('TRUE')

else: print('FALSE')    