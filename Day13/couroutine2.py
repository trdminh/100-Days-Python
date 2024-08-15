from time import sleep
from inspect import getgeneratorstate

def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        print('Số chuyển phát nhanh %d đã sẵn sàng nhận đơn hàng hôm nay %d.' % (man_id, total))
        pkg = yield
        print('Số chuyển phát nhanh %d đã nhận được số gói hàng %s.' % (man_id, pkg))
        sleep(0.5)

def package_center(deliver_man, max_per_day):
    num = 1
    print(getgeneratorstate(deliver_man))
    deliver_man.send(None)

    print(getgeneratorstate(deliver_man))

    while num <= max_per_day:
        package_id = 'PKG-%d' % num
        deliver_man.send(package_id)
        num += 1
    deliver_man.close()

    print(getgeneratorstate(deliver_man))
    print('今天的包裹派送完毕!')


dm = build_deliver_man(1)
package_center(dm, 10)