def main():
    stu = {'name':'Minh','age':20,'gender':'male'}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for elem in stu:
        print(elem)
        print(elem[0], elem[1])
    print(stu)
    stu.setdefault('score', 60)
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)



if __name__ == '__main__':
    main()