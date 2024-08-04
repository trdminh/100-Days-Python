def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['banana', 'pear','tomato']
    print(fruits)
    for fruit in fruits:
        print(fruit.title(),end=' ')
    fruits2 = fruits[1:4]
    print(fruits2)
    fruits3 = fruits[:3]
    print(fruits3)
    fruits4 = fruits[2:]
    print(fruits4)
    fruits5 = fruits[::-1]
    print(fruits5)
    fruits6 = fruits[:]
    print(fruits6)


if __name__ == '__main__':
    main()