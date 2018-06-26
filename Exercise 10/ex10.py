def radix_sort(L):
    '''(list) -> list
    Takes a list of integers and returns a list with the same integers sorted
    in non-decreasing order.
    REQ: aList is a list of integers.
    >>> radix_sort([240, 28, 5, 18, 140, 2])
    [2, 5, 18, 28, 140, 240]
    '''
    aList = L[:]
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for i in range(RADIX)]
        # split aList between lists
        for i in aList:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False
        # empty lists into aList array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1
        # move to next digit
        placement *= RADIX
    return aList
