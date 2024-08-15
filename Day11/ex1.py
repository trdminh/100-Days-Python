input_again = True
while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d / %d = %f' % (a, b, a / b))
        input_again = False
    except ValueError:
        print('Gia tri vao khong hop le')
    except ZeroDivisionError:
        print('Khong co ket qua')