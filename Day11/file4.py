import base64

filename = '/home/minh/Documents/Code/python/100dayspython/Day11/mm.jpg'

with open(filename,'rb') as f:
    data = f.read()
    print(len(data))
    #print(base64.b64encode(data))

with open('filename', 'wb') as f:
    f.write(data)
print('写入完成!')