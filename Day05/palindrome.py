'''
Xác định xem số nguyên dương đầu vào có phải là số palindrome hay không
Số palindrome đề cập đến một số nguyên dương có cùng giá trị khi được sắp xếp từ trái sang phải cũng như khi sắp xếp từ phải sang trái.
'''

num = int(input('Nhap gia tri: '))

temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp%10
    temp //= 10

if num2 == num:
    print('TRUE') 
else:
    print('FALSE')