
def main():
    set1 = {1,2,3,4,5}
    print(set1)
    print('Length = ',len(set1))
    set2 = set(range(1,11))
    print(set2)
    print('Length = ',len(set2))
    set1.add(6)
    set1.add(7)
    print(set1)
    set2.update([11,12])
    set2.discard(5)
    print(set2)
    if 3 in set2:
        set2.remove(3)
    print(set2)
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)


if __name__ == '__main__':
    main()