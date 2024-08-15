class Car(object):
    def __init__(self,brand,max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand
    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%s toc do hien tai %d' % (self._brand, self._current_speed)
    
class Student(object):
    def __init__(self,name,age) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    def driver(self,car):
        print('%s dang lai xe %s'%(self._name,car._brand))
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        car.accelerate(50)
        print(car)

    def study(self,course_name):
        print('%s dang hoc %s '%(self._name,course_name))
    
    def watch_av(self):
        if self._age < 18:
            print('%s khong du tuoi lai xe'%self._name)
        else:
            print('%s du tuoi lai xe'%self._name)

    def __gt__(self, other):
        return self._age > other._age


    def __lt__(self, other):
        return self._age < other._age



if __name__ == '__main__':
    stu1 = Student('Minh', 20)
    stu1.study('Python')
    stu1.watch_av()
    stu2 = Student('Long', 15)
    stu2.study('Math')
    stu2.watch_av()
    car = Car('BMW', 120)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu1 < stu2)