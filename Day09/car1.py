class Car(object):
    __slots__ = ('_brand','_max_speed')

    def __init__(self,brand,max_speed):
        self._brand = brand
        self._max_speed = max_speed
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self,brand):
        self._brand = brand
    
    @brand.deleter
    def brand(self):
        del self._brand

    @property
    def max_speed(self):
        return self._max_speed
    
    @max_speed.setter
    def max_speed(self,max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed
    def __str__(self):
        return 'Car: [Hang xe %s, Toc do toi da %d]' % (self._brand, self._max_speed)

car = Car('Vinfast',250)
print(car)
car.max_speed = 320
car.brand = "BMW"
print(car)

print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
print(Car.brand.fdel)