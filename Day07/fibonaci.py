def fibonaci():
    f = [0,1]
    for i in range(2, 20):
        #f += [f[i - 1] + f[i - 2]]
        f.append(f[i - 1] + f[i - 2])
    for val in f:
        print(val, end=' ')

if __name__ == '__main__':
    fibonaci()
    print()