def f1(a, b=5, c=10):
    return a + b*2 + c*3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))

def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())

def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是: %s!' % kw['tel'])
    else:
        print('没找到你的个人信息!')


param = {'name': 'Minh', 'age': 38}
f3(**param)
f3(name='Minh', age=38, tel='13866778899')
f3(user='Minh', age=38, tel='13866778899')
f3(user='Minh', age=38, mobile='13866778899')
