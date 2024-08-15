def main():
    num = int(input('Nhap so cot: '))
    y = [[]]*num
    for row in range(len(y)):
        y[row] = [None] * (row + 1)
        for col in range(len(y[row])):
            if col == 0 or col == row:
                y[row][col] = 1
            else:
                y[row][col] = y[row - 1][col] + y[row - 1][col - 1]
            print(y[row][col], end='\t')
        print()

main()