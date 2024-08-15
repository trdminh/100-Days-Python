import re

def main():
    username = input('Nhap ten dang nhap: ')
    qq = input('Nhap so qq: ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('Vui long nhap ten hop le.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')

main()