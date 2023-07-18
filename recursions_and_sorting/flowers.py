def flowers(array):
    if len(array) == 1:
        return array
    left = flowers(array[0 : len(array)//2])
    right = flowers(array[len(array)//2 : len(array)])
    result = [[] for i in range(len(array))]
    #print(result, left, right)
    
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right): 
        if not left[l]:
            left[l] = result[k-1]
        if not right[r]:
            right[r] = result[k-1]
        if left[l][1] < right[r][0] or right[l][1] < left[r][0]:
            if left[l][0] <= right[r][0]: 
                result[k] = left[l]
                l += 1
            else:
                result[k] = right[r]
                r += 1
            k += 1
            #print('kkk')
            #print(result)
        elif left[l] <= right[r]:
            result[k] = [left[l][0], max(right[r][1], left[l][1])]
            l += 1
            k += 1
            r += 1   
            #print('ooo')
            #print(result, l, k, r)
            #print(left, right)
        else:
            result[k] = [right[r][0], max(right[r][1], left[l][1])]
            l += 1
            k += 1
            r += 1
            #print(sdfsdfsd)
    while l < len(left): 
        if left[l] not in result:
            result[k] = left[l]
        l += 1
        k += 1  
    while r < len(right): 
        if right[r] not in result:
            result[k] = right[r]
        r += 1
        k += 1
    return result


if __name__ == '__main__':
    n = int(input())
    numbers = [[int(i) for i in input().split()] for _ in range(n)]
    rez = flowers(numbers)
    rez_for_print = []
    for i in rez:
        if i and i not in rez_for_print:
            rez_for_print.append(i)
    for i in rez_for_print:
        print(*i)
        
        
        
