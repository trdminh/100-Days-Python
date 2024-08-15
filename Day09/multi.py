class Father(object):
    def __init__(self,name):
        self._name = name

    def gamble(self):
        print('%s choi bai'%self._name)

    def eat(self):
        print('%s an com'%self._name)


class Monk(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s dang an.' % self._name)

    def chant(self):
        print('%s .' % self._name)


class Musician(object):

    def __init__(self, name):
        self._name = name

    def play_piano(self):
        print('%s dang choi dan.' % self._name)

class Son(Father, Monk, Musician):

    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)

son = Son('Minh')
son.gamble()
son.eat()
son.chant()
son.play_piano()