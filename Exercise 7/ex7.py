def rsum(L):
    '''(list) -> int
    Return the sum of all elements in a given list.
    REQ: L is not empty.
    '''
    if not isinstance(L, list):
        result = L
    elif L == []:
        result = 0
    else:
        result = rsum(L[0]) + rsum(L[1:])
    return result


def rmax(L):
    '''(list) -> int
    Return the maximum number in a given list.
    REQ: L is not empty.
    '''
    if not isinstance(L, list):
        result = L
    elif L == []:
        result = -float("inf")
    else:
        max = rmax(L[0])
        result = rmax(L[1:])
        if max > result:
            result = max
    return result


def second_smallest(L):
    '''(list) -> int
    Return the second smallest number in a given list.
    REQ: L has at least 2 elements.
    '''
    return finds(L)[1]


def finds(l):
    '''(list) -> (int, int)
    Return a tuple of the 2 minimum elements in a given list.
    REQ: l is not empty.
    REQ: l has at least 2 elements.
    '''
    n = len(l)
    if n >= 2:
        f1, s1 = finds(l[:n//2])
        f2, s2 = finds(l[n//2:])
        if f1 is None:
            return f2, s2
        elif f2 is None:
            return f1, s1
        elif f1 < f2:
            return f1, (f2 if s1 is None or s1 > f2 else s1)
        else:
            return f2, (f1 if s2 is None or s2 > f1 else s2)
    if n == 0:
        return None, None
    elif isinstance(l[0], list):
        return finds(l[0])
    else:
        return l[0], None


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
    length = len(L)
    if length > 1:
        mid = length // 2
        result = find(L[:mid])
        result2 = find(L[mid:])
        if (result2[0] < result[0]):
            result[0] = result2[0]
        if (result2[1] > result[1]):
            result[1] = result2[1]
        return result
    elif length == 1:
        if isinstance(L[0], list):
            return find(L[0])
        else:
            return [L[0], L[0]]
    else:
        return [float('inf'), -float('inf')]
