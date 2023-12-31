def buy_bicycle(arr, x, left, right):
    if x <= arr[0]:
        return 1
    if right <= left or x > arr[-1]:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x and arr[mid-1] < x:
        return mid + 1
    elif arr[mid] >= x:
        return buy_bycicle(arr, x, left, mid)
    else:
        return buy_bycicle(arr, x, mid + 1, right)


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    price = int(input())
    print(buy_bicycle(arr, price, left=0, right=len(arr)), end=' ')
    print(buy_bicycle(arr, price * 2, left=0, right=len(arr)))
