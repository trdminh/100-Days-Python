def __foo():
    print('test')

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def study(self,course_name):
        print('%s dang hoc mon %s'%(self.name,course_name))
    
    def watch_av(self):
        if self.age > 18:
            print('%s co the chay xe may'%self.name)
        else:
            print('%s khong duoc chay xe may'%self.name)


def main():
    stu1 = Student('Minh', 20)
    stu1.study('Python')
    stu1.watch_av()
    stu2 = Student('Nam', 15)
    stu2.study('Toan')
    stu2.watch_av()


if __name__ == '__main__':
    main()