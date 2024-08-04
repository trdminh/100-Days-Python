def main():
    scores = {'toan':10,'van':8,'anh':7}
    print(scores['anh'])
    print(scores['toan'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['anh'] = 9
    scores.update(ly = 8 , sinh=10)
    if 'ly' in scores:
        print(scores['ly'])
    print(scores.get('anh'))
    print(scores.get('van',10))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('anh',1))
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()