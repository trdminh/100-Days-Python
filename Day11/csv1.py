import csv

filename = '/home/minh/Documents/Code/python/100dayspython/Day11/example.csv'

try:
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('khong the mo file: ',filename)

else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))