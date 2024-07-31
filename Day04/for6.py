n = int(input('Nhap n:'))

for i in range(0,n):
    for _ in range(0,i+1):
        print('*',end='')
    print()

for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()