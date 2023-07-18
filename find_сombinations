def find_сombinations(keypad, keys, combinations, index, result=''):
    if index == -1:
        combinations.append(result)
        return
    digit = keys[index]
    length = len(keypad[digit])
    for i in range(length):
        find_сombinations(keypad, keys, combinations, index - 1, keypad[digit][i] + result)


if __name__ == '__main__':
    keypad = {'2':'abc',
             '3':'def',
             '4':'ghi',
             '5':'jkl',
             '6':'mno',
             '7':'pqrs',
             '8':'tuv',
             '9':'wxyz'}
    keys = list(input())
    combinations = list()
    answer = find_сombinations(keypad, keys, combinations, len(keys) - 1)

    print(*sorted(combinations))
