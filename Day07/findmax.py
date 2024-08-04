def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    print(max(fruits))
    print(min(fruits))
    max_value = min_value = fruits[0]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]
    print('Max:', max_value)
    print('Min:', min_value)


if __name__ == '__main__':
    main()