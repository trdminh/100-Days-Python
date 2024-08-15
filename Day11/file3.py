from math import sqrt

def is_prime(n):
    for index in range(2,int(sqrt(n)+1)):
        if n % index == 0:
            return False
    return True

filename = '/home/minh/Documents/Code/python/100dayspython/Day11/prime.txt'

with open(filename,'w') as f:
    for num in range(2, 100):
        if is_prime(num):
            f.write(str(num) + '\n')

print('Done')