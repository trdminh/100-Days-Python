def bar(self,name):
    self._name = name

def foo(self, course_name):
    print('%s hien dang hoc %s.' % (self._name, course_name))

def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = Student('Minh')
    stu1.study('Python')

main()