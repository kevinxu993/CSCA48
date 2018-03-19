def greeting(name):
    '''(str) -> str
    Takes a string as a parameter that represents a person's name, and returns
    a greeting in the form "Hello <name> how are you today?" where <name> is
    replaced by the given name.
    REQ: name is a string that represents a person's name.
    >>> greeting("Kevin")
    'Hello Kevin how are you today?'
    '''
    # create a string to be returned
    result = 'Hello ' + name + ' how are you today?'
    # return the string
    return result


def mutate_list(LIST):
    '''(list) -> None
    Takes a list as a parameter, and modifies that list in the following ways:
    1. Any element that is an integer is multipled by 2. Any element that is a
    boolean is inverted (True becomes False, False becomes True). 3. Any
    element that is a string has its first and last characters removed. 4. The
    0th element of the list is set to the string 'Hello', regardless of what it
    was originally.
    REQ: LIST should have at least 1 element in it.
    REQ: All strings should have at least 2 characters in them.
    >>> mutate_list(['abc', 1, 2.5, True, False, [3, 4, 5]])

    '''
    # The 0th element of the list is set to the string 'Hello'
    LIST[0] = 'Hello'
    # search the list from the second element
    for i in range(1, len(LIST)):
        # string has its first and last characters removed
        if(isinstance(LIST[i], str)):
            LIST[i] = LIST[i][1:-1]
        # boolean is inverted (True becomes False, False becomes True)
        elif(isinstance(LIST[i], bool)):
            LIST[i] = not LIST[i]
        # integer is multipled by 2
        elif(isinstance(LIST[i], int)):
            LIST[i] = LIST[i] * 2


def merge_dicts(dic1, dic2):
    '''(dict, dict) -> dict
    Takes two dictionaries as input, both of the format {str: list of ints}.
    The function returns a new dictionary with all key:value pairs from both
    dictionaries. If the dictionaries share a key, the resulting value will be
    the list from the second dictionary appended to the list from the first
    dictionary.
    REQ: dic1 and dic2 are both of the format {str: list of ints}.
    >>> merge_dicts({'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}, {'a': [2]})
    {'a': [1, 2, 3, 2], 'b': [4], 'c': [5, 6, 7]}
    '''
    # create a dictionary to be returned
    dic = {}
    # copy the first dictionary
    for i in dic1:
        dic[i] = dic1[i][:]
    # add keys from dic2 to the new dictionary
    for i in dic2:
        # if dic1 has this key
        if i in dic:
            # add the new value to that key
            dic[i] = dic[i] + dic2[i]
        # if not
        else:
            # add the new key to the dictionary
            dic[i] = dic2[i]
    return dic
