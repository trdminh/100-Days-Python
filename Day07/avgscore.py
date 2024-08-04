def main():
    number = int(input('Nhap so luong mon hoc: '))
    names = [None] * number
    scores = [None] * number
    for index in range(len(names)):
        names[index] = input('Mon hoc thu %d: ' % (index + 1))
        scores[index] = float(input('Diem cua mon hoc thu% d: ' % (index + 1)))
    total = 0
    for index in range(len(names)):
        print('%s: %.1f diem' % (names[index], scores[index]))
        total += scores[index]
    print('Diem trung binh: %.1fdiem' % (total / number))


if __name__ == '__main__':
    main()