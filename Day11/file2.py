birth = input('Vui long nhap ngay sinh cua ban: ')
with open('/home/minh/Documents/Code/python/100dayspython/Day11/pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print('Bingo!!!')