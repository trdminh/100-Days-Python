'''
Người chơi tung hai viên xúc xắc. Nếu lần tung đầu tiên ra 7 hoặc 11, người chơi sẽ thắng.
Nếu ra được 2 điểm, 3 điểm hoặc 12 điểm thì nhà cái thắng.
Người chơi yêu cầu tung xúc xắc lần nữa. Nếu tung được 7 điểm thì nhà cái thắng.
Nếu số của lần đổ đầu tiên được rút ra thì người chơi sẽ thắng.
Nếu không, trò chơi vẫn tiếp tục và người chơi tiếp tục tung xúc xắc.
Người chơi bước vào trò chơi với số tiền đặt cược là 1.000 nhân dân tệ và trò chơi sẽ kết thúc nếu tất cả đều thua.


'''

from random import randint

money = 1000
while money > 0:
    print("So tien dang co: %d"%money)
    need_to_go = False
    while True:
        debt = int(input('Nhap vao so tien muon cuoc: ')) 
        if 0 <= debt <= money:
            break
    first = randint(1,6) + randint(1,6)
    print('So diem dat duoc %d'%first)
    if first == 7 or first == 11:
        money += debt
    elif first == 2 or first == 3 or first == 12:
        money -= debt
    else: need_to_go = True
    while need_to_go:
        current = randint(1,6) + randint(1,6)
        print('So diem dat duoc %d' % current)
        if current == 7:
            print('I am sorry')
            money -= debt
            need_to_go = False
        elif current == first:
            print('Bingo!')
            money += debt
            need_to_go = False


