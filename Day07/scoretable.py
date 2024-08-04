def main():
    names = ['minh','tuan','thang','trung','nam']
    subjects = ['toan','van','anh']
    scores = [[0]*3]*5
    for row, name in enumerate(names):
        print('Vui long nhap so diem cua %s' % name)
        for col, subj in enumerate(subjects):
            scores[row][col] = float(input(subj + ': '))
    print(scores)

if __name__ == '__main__':
    main()