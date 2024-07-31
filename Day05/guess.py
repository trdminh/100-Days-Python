import random

answer = random.randint(1, 100)
counter = 0
while True:
    number = int(input('Nhap vao gia tri du doan: '))
    counter += 1
    if number > answer:
        print('Lon hon mat roi')
    elif number < answer:
        print('Nho hon mat roi')
    else:
        print('Bingo!')
        break

if counter > 7:
    print('To bad!')