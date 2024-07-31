
'''

Giải bài toán “Trăm xu và trăm con gà”
1 con gà trống 5 nhân dân tệ 1 con gà mái 3 nhân dân tệ 3 con gà con 1 nhân dân tệ Mua 100 con gà với 100 nhân dân tệ
Hỏi có bao nhiêu con gà trống, gà mái và gà con?
'''
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('Ga trong: %dcon, Ga mai: %dcon, Ga con: %dcon' % (x, y, z))