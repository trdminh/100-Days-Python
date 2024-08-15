import csv

class Teacher(object):
    def __init__(self,name,age,title):
        self._name = name
        self._age = age
        self._title = title
        self._index = -1

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def title(self):
        return self._title
    
filename = '/home/minh/Documents/Code/python/100dayspython/Day11/teacher.csv'
teachers = [Teacher('Minh',20,'Math'),Teacher('Long',39,'English')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writerow([teacher.name,teacher.age,teacher.title])
except BaseException as e:
    print('Khong the viet vao file: ',filename)

else:
    print('Da ghi xong')


    