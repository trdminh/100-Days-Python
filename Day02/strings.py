
str1 = 'hello, world!'
print('Do dai chuoi:', len(str1))
print('Viet hoa chu dau: ', str1.title())
print('Viet hoa toan bo: ', str1.upper())
# str1 = str1.upper()
print('Tat ca cac ky tu la viet hoa: ', str1.isupper())
print('Bat dau bang tu hello: ', str1.startswith('hello'))
print('Ket thuc bang tu hello: ', str1.endswith('hello'))
print('Bat dau bang ky tu !: ', str1.startswith('!'))
print('Ket thuc bang ky tu !: ', str1.endswith('!'))
str2 = '- \u9a21\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)