from random import randint

class GuessMachine(object):
    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None
    def reset(self):
        self._answer = randint(1,100)
        self._counter = 0
        self._hint = None
    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = 'Lon hon mat roi'
        elif your_answer < self._answer:
            self._hint = 'Nho hon mat roi'
        else:
            self._hint = 'Bingo!'
            return True
        return False
    
    @property
    def counter(self):
        return self._counter
    
    @property
    def hint(self):
        return self.hint

if __name__ == '__main__':
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input('Nhap gia tri: '))
            game_over = gm.guess(your_answer)
            print(gm._hint)
        play_again = input('Choi tiep?(yes|no)') == 'yes'