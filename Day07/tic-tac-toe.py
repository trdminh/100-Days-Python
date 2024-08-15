import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        while counter < 9:
            move = input('Den luot %s di chuyen '%turn)
            if curr_board == ' ':
                counter+=1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else: turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('Choi lai (yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
