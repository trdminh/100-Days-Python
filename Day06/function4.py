import time
import shutil
import os

seconds = time.time()
print(seconds)

localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

shutil.copy('/home/minh/Documents/Code/python/100dayspython/Day06/function1.py', '/home/minh/Documents/Code/python/100dayspython/Day06/function2.py')
os.system('ls -l')
os.chdir('/home/minh/Documents/Code/python/100dayspython/Day06')
os.system('ls -l')
os.mkdir('test')