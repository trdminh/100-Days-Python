
value = float(input('Nhap gia tri: '))
unit = input('Nhap don vi: ')
if unit == 'in':
    print('%fin = %fcm' % (value, value * 2.54))
elif unit == 'cm':
    print('%fcm = %fin' % (value, value / 2.54))
else:
    print('Khong xac dinh')