import time
import csv
import sys
filename = input('Nhap ten file: ')

try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError as msg:
    print(msg)
except UnicodeDecodeError as msg:
    print('Không thể giải mã được các tệp không phải văn bản')
    sys.exit()
else:
    for line in lines:
        print(line.rstrip())
        time.sleep(0.5)
finally:
    # 此处最适合做善后工作
    print('不管发生什么我都会执行')