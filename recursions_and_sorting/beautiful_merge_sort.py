def merge(array, lf, mid, rg):
    l, r = 0, 0
    result = []
    left = array[lf:mid]
    right = array[mid:rg]
    while l < len(left) and r < len(right): 
        if left[l] <= right[r]: 
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left): 
        result.append(left[l])
        l += 1
    while r < len(right): 
        result.append(right[r])
        r += 1
    return result


def merge_sort(array, lf, rg):
    if rg - lf > 1:
        mid = (lf + rg) // 2
        merge_sort(array, lf, mid)
        merge_sort(array, mid, rg)
        array[lf:rg] = merge(array, lf, mid, rg)


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected


if __name__ == '__main__':
    test()
