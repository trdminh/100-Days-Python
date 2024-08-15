def main():
    t = ('minh',20,True,'Nam Dinh')
    print(t)

    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])

    for member in t:
        print(member)
    
    t = list(t)
    print(t)
    t[0] = 'nam'
    t[1] = 25
    print(t)
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(fruits_tuple[1])

main()