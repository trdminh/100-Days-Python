from math import sqrt


class Triangle(object):
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
    

    @staticmethod
    def is_value(a,b,c):
        return a+b>c and a+c>b and b+c>a
    
    def perimeter(self):
        return self._a + self._b + self._c
    
    def area(self):
        p = (self._a + self._b + self._c)/2
        return sqrt(p*(p-self._a)*(p-self._b)*(p-self._c))
    

if __name__ == '__main__':
    a,b,c = map(float,input('Nhap do dai 3 canh:').split())
    if Triangle.is_value(a, b, c):
        tri = Triangle(a, b, c)
        print('Chu vi:', tri.perimeter())
        print('Dien tich:', tri.area())

    else:
        print('Khong phai hinh tam giac')
        