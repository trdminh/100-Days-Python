from multiprocessing import Process, Queue, current_process
from time import sleep
import random

def sub_task(content, counts):
    print(f'PID: {current_process().pid}')
    counter = 0
    while counter < counts:
        counter += 1
        print(f'{counter}: {content}')
        sleep(0.01)


def main():
    number = random.randrange(5, 10)
    Process(target=sub_task, args=('Ping', number)).start()
    Process(target=sub_task, args=('Pong', number)).start()


if __name__ == '__main__':
    main()