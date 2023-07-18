def comparator(num_1, num_2):
    if len(num_1) == len(num_2):
        return num_1 > num_2
    var_1 = num_1 + num_2
    var_2 = num_2 + num_1 
    return var_1 > var_2


def biggest_number(array, key):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and key(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    return ''.join(array)


if __name__ == '__main__':
    n = int(input())
    numbers = input().split()
    print(biggest_number(numbers, comparator))
