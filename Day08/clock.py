import os
import time

class Clock():
    def __init__(self, **kw) :
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self.__hour = kw['hour']
            self.__minute = kw['minute']
            self.__second = kw['second']
        else:
            tm = time.localtime()
            self.__hour = tm.tm_hour
            self.__minute = tm.tm_min
            self.__second = tm.tm_sec
    def run(self):
        self.__second += 1
        if self.__second == 60:
            self.__minute += 1
            self.__second = 0
            if self.__minute == 60:
                self.__hour += 1
                self.__minute = 0
                if self.__hour == 24:
                    self.__hour = 0
    def show(self):
        return '%02d:%02d:%02d' % (self.__hour, self.__minute, self.__second)
    
if __name__ == '__main__':
    clock = Clock()
    while True:
        os.system('clear')
        print(clock.show())
        time.sleep(1)
        clock.run()