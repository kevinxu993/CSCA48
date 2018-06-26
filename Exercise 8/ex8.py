def edit_distance(s1, s2):
    ''' (str, str) -> int
    Returns the number of single character changes
    necessary to turn s1 into s2.
    '''
    if len(s1) == 0:
        result = 0
    else:
        cost = 0
        if s1[0] != s2[0]:
            cost = 1
        result = cost + edit_distance(s1[1:], s2[1:])
    return result


def subsequence(s1, s2):
    ''' (str, str) -> bool
    s1 is a subsequence of s2 iff s2 can be made equal to s1 by removing 0 or
    more of its characters. Return True iff s1 is a subsequence of s2.
    '''
    # base cases
    if s1 == s2:
        result = True
    # if s1 is empty, all empty strings are subsequences of all other strings
    elif not s1:
        result = True
    # if s1 is longer than s2, s1 cannot possibly be substring of s2
    elif len(s1) > len(s2):
        result = False
    # recursion step
    else:
        # check the chars at first index
        if s1[0] == s2[0]:
            # recursively call the rest of the 2 strings
            result = subsequence(s1[1:], s2[1:])
        else:
            # otherwise, remove that char from s2 and recursively call the rest
            result = subsequence(s1, s2[1:])
    return result


def perms(s):
    ''' (str) -> set of str
    Given a string s, return a set of all possible permutations of the
    letters in s.
    '''
    # initialize a return set
    ret = set()
    # base cases: if s is empty
    if not s:
        return {''}
    # if s is only a char
    if len(s) == 1:
        return set(s)
    # recursion step
    else:
        # return the permutated list of a smaller string namely, s w/o the
        # first char
        permed = perms(s[1:])
        # for every element in the set
        for elmt in permed:
            # here I want to loop through all the possible index from 0 to
            # len(elmt) + 1
            for i in range(len(elmt)+1):
                # insert s[0] in between all possible indices i
                new_s = elmt[:i] + s[0] + elmt[i:]
                # add the element into the set
                ret.add(new_s)
        return ret
