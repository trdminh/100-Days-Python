x = int(input('x = '))
y = int(input('y = '))
if x > y:
    (x, y) = (y, x)
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('Uoc chung lon nhat cua %d va %d la %d' % (x, y, factor))
        print('Boi chung nho nhat cua %d va %d la %d' % (x, y, x * y // factor))
        break