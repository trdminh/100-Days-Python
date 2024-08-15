def bubble_sort(origin_items, comp=lambda x, y: x > y):
    items = origin_items[:]
    for i in range(1,len(items)):
        swapper = False
        for j in range(i - 1, len(items) - i):
            if comp(items[j],items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapper = True
            
        if swapper:
            swapper = False
            for j in range(len(items) - 1 - i, i - 1, -1):
                if comp(items[j - 1], items[j]):
                    items[j - 1], items[j] = items[j], items[j - 1]
                    swapper = True
        
        if not swapper:
            break
    
    return items

def select_sort(origin_items, comp=lambda x, y: x < y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1,len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    
    return items


def merge(items1, items2, comp=lambda x, y: x <= y):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1],items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    
    items += items1[index1:]
    items += items2[index2:]
    return items

def merge_sort(items, comp=lambda x, y: x <= y):
    if len(items) < 2:
        return items[:]
    mid = len(items)//2
    left = merge_sort(items[:mid],comp)
    right = merge_sort(items[mid:],comp)
    return merge(left,right)


def partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start,end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i+1], items[end] = items[end], items[i+1]
    return i+1

def _quick_sort(items, start, end, comp):
    """递归调用划分和排序"""
    if start < end:
        pos = partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)
def quick_sort(origin_items, comp=lambda x,y: x < y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items

class Person(object):
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __gt__(self, other):
    #     return self.name > other.name

    def __str__(self):
        return f'{self.name}: {self.age}'

    def __repr__(self):
        return self.__str__()

def main():
    """主函数"""
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    # print(bubble_sort(items))
    # print(select_sort(items))
    # print(merge_sort(items))
    print(quick_sort(items))
    items2 = [
        Person('Wang', 25), Person('Luo', 39),
        Person('Zhang', 50), Person('He', 20)
    ]
    # print(bubble_sort(items2, comp=lambda p1, p2: p1.age > p2.age))
    # print(select_sort(items2, comp=lambda p1, p2: p1.name < p2.name))
    # print(merge_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    print(quick_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
    # print(bubble_sort(items3))
    # print(bubble_sort(items3, comp=lambda x, y: len(x) > len(y)))
    # print(merge_sort(items3))
    print(merge_sort(items3))


if __name__ == '__main__':
    main()