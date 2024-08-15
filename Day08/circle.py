import math

class Circle(object):
    def __init__(self,radius) :
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self,radius):
        self.__radius = radius if radius > 0 else 0
    
    @property
    def perimeter(self):
        return 2*math.pi * self.__radius
    
    @property
    def area(self):
        return (self.__radius**2)*math.pi

if __name__ == '__main__':
    radius = float(input('Nhap gia tri cua ban kinh: '))
    small = Circle(radius)
    big = Circle(radius+3)
    print(big.perimeter)
    print(big.area - small.area)