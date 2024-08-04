import math

a = float(input('Do dai canh thu nhat = '))
b = float(input('Do dai canh thu hai = '))
c = float(input('Do dai canh thu ba = '))

if a + b > c and a + c > b and b + c > a:
    print('Chu vi cua tam giac = %f' % (a+b+c))
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('Dien tich cua tam giac = %f' % area)

else:
    print('Khong phai 3 canh cua tam giac')