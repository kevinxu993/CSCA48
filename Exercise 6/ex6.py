def rsum(L):
    '''(list) -> int
    Return the sum of all elements in a given list.
    REQ: L is not empty.
    '''
    # Base case: length is 1
    if len(L) == 1:
            result = L[0]
    else:
        # add the first number to the sum of the rest of L
        result = L[0] + rsum(L[1:])

    return result


def rmax(L):
    '''(list) -> int
    Return the maximum number in a given list.
    REQ: L is not empty.
    '''
    # Base case: length is 1
    if len(L) == 1:
        result = L[0]
    else:
        # compare the number with the first number in the sliced list
        max = rmax(L[1:])
        if L[0] > max:
            result = L[0]
        else:
            result = max

    return result


def second_smallest(L):
    '''(list) -> int
    Return the second smallest number in a given list.
    REQ: L has at least 2 elements.
    '''
    (min2, min) = finds(L)

    return min2


def finds(L):
    '''(list) -> (int, int)
    Return a tuple of the 2 minimum elements in a given list.
    REQ: L is not empty.
    REQ: L has at least 2 elements.
    '''
    # Base case: length is 2
    if len(L) == 2:
        # if the first element is bigger or equal to the second element
        if L[0] >= L[1]:
            result = (L[0], L[1])
        else:
            result = (L[1], L[0])
    else:
        # compare the numbers with the first element in the sliced list
        (min2, min) = finds(L[1:])
        if L[0] < min:
            min, min2 = min2, min
            min = L[0]
        elif L[0] < min2:
            min2 = L[0]
        result = (min2, min)

    return result


def sum_max_min(L):
    '''(list) -> int
    Return the sum of the maximum and minimum elements in a given list.
    REQ: L is not empty.
    '''

    (max, min) = find(L)
    return max + min


def find(L):
    '''(list) -> (int, int)
    Return a tuple of the maximum and minimum elements in a given list.
    REQ: L is not empty.
    '''
    # Base case: length is 1
    if len(L) == 1:
        result = (L[0], L[0])
    # Base case: length is 2
    elif len(L) == 2:
        # if the first element is bigger or equal to the second element
        if L[0] >= L[1]:
            result = (L[0], L[1])
        else:
            result = (L[1], L[0])
    else:
        # compare the numbers with the first element in the sliced list
        (max, min) = find(L[1:])
        if L[0] > max:
            max = L[0]
        if L[0] < min:
            min = L[0]
        result = (max, min)

    return result
