from math import sqrt

num = int(input('Nhap gia tri n: '))
end = int(sqrt(num))

is_prime = True

if num == 2: 
    is_prime = True
else:
    for i in range(2, end+1):
        if num % i == 0:
            is_prime = False
            break

if is_prime == True and num != 1:
    print('%d la so nguyen to'%num)

else: print('%d khong la so nguyen to'%num)