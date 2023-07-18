def bubbles(numbers, good):
    count = 0
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            count += 1
    if count > 0:
        good = False
        print(*numbers)
        bubbles(numbers, good)
    elif good:
        print(*numbers)


if __name__ == '__main__':
    n = int(input())
    numbers = [int(i) for i in input().split()]
    bubbles(numbers, good = True)
