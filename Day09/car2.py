class Car(object):
    def __init__(self, brand, max_speed):
        self.set_brand(brand)
        self.set_max_speed(max_speed)

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [Hang xe %s, Toc do toi da %d]' % (self._brand, self._max_speed)

    brand = property(get_brand, set_brand)
    max_speed = property(get_max_speed, set_max_speed)
    
car = Car('Vinfast',250)
print(car)
car.max_speed = 320
car.brand = "Benz"
print(car)
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)