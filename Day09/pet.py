from abc import ABCMeta, abstractmethod

class Pet(object, metaclass = ABCMeta):
    def __init__(self,nickname):
        self._nickname = nickname

    @abstractmethod
    def voice(self):
        pass

class Dog(Pet):
    def voice(self):
        print('%s gau gau'%self._nickname)

class Cat(Pet):
    def voice(self):
        print('%s meow meow'%self._nickname)


def main():
    pets = [Dog('Nick'),Cat('Lyly'),Dog('John')]
    for pet in pets:
        pet.voice()

main()