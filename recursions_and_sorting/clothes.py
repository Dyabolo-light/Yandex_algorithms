from itertools import chain


def clothes_counting(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1
    new = [[i for _ in range(counted_values[i])] for i in range(k)]
    return list(chain.from_iterable(new))


if __name__ == '__main__':
    n = int(input())
    array = [int(i) for i in input().split()]
    print(*clothes_counting(array, 3))
