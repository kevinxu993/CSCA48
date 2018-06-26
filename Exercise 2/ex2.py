from container import *


def banana_verify(sw, gw, ctn, move):
    '''(str, str, Container, list of str) -> bool
    Takes 4 parameters: a source word, goal word, a container, a list of moves.
    The source and goal words are the source and goal words for the banana
    game. The list of moves is a list of moves, with M meaning move, P meaning
    put, and G meaning get. Returns True only if the moves in the moves list,
    preformed using the specified container will turn the source word into the
    goal word.
    REQ: sw is a str. gw is a str. ctn is a Container object. move is a
    list of str.
    >>> banana_verify('CAT', 'ACT', Container, ['P', 'M', 'G', 'M'])
    True
    '''
    # if no source is given
    if len(sw) == 0:
        # return False as result
        return False
    # create an empty string
    goal = ''
    # check every move in the list of moves
    for i in move:
        # if no exception
        try:
            # if Move
            if i == 'M':
                # add next letter to goal
                goal = goal + sw[0]
                # cut the last letter from source
                sw = sw[1:len(sw)]
            # if Put
            elif i == 'P':
                # put next letter to container
                ctn.put(sw[0])
                # cut the last letter from source
                sw = sw[1:len(sw)]
            # if Get
            elif i == 'G':
                # store the letter popped from container
                temp = ctn.get()
                # add the letter to goal
                goal = goal + temp
        # if exception
        except (ContainerFullException, ContainerEmptyException):
            # result is False
            result = False
            # return the result
            return result
    # if source and container are empty, as well as goal is achieved
    if ((len(sw) == 0) and (ctn.is_empty()) and (goal == gw)):
        # result is True
        result = True
    # if not
    else:
        # result is False
        result = False
    # return the result
    return result
