from week4_DLL import DNode, DoubleLinkedList


def reverse_merge(list1, list2):
    '''(DoubleLinkedList, DoubleLinkedList) -> DoubleLinkedList
    Takes two double linked lists as input parameters. The first linked list
    contains the surnames of Marzieh's students in CSCA48 sorted ascendingly
    and the second contains Nick's students' surnames for the same course
    sorted in a descending order. Returns a DLL containing all of the students'
    surnames sorted ascendingly.
    REQ: list1 and list2 are double linked lists.
    REQ: list1 has names in ascending order.
    REQ: list2 has names in descending order.
    '''
    # create a new DLL
    new = DoubleLinkedList()
    # copy names in list1 to the new list
    curr = list1._head._next
    while(curr != list1._tail):
        new.add_last(curr._element)
        curr = curr._next

    # check every name in list2
    now = list2._head._next
    while(now != list2._tail):
        # compare this name to every name in list1
        curr = new._head._next
        while(curr != new._tail) and (now._element >= curr._element):
            curr = curr._next
    # set the next list2 name to check
        nextnode = now._next
    # if this name can be inserted in the new list
        if now._element != (curr._element and curr._prev._element):
            # insert the name
            now.set_next(curr)
            now.set_prev(curr._prev)
            curr.set_prev(now)
            now._prev.set_next(now)
            new._size = new._size + 1

    # set the next list2 name to check
        now = nextnode

    # return the new list
    return new


def allocate_room(L, room, cap, ind):
    '''(DoubleLinkedList, str, int, int) -> str
    Takes four parameters; a dll containing students' surnames, a string
    representing a room name and number, an int representing the capacity of
    the room and an int representing the index of the node that contains the
    surname of the first person that is assigned to this room. Returns a string
    that shows the two first letters of the surnames of the first and the last
    person that should attend the given room.
    REQ: L is a DLL containing names in ascending order
    REQ: room is a string representing a room name and number
    REQ: cap is an int representing the capacity of the room
    REQ: ind is an int representing the index of the node that contains the
    REQ: surname of the first person that is assigned to this room
    '''
    # create a string to be part of the result
    result = room + " "
    # get the beginning of the list
    curr = L._head._next
    # set a number to check the number of names
    num = 0
    # set a goal index of the name
    goal = cap + ind - 1
    # check the list
    while(curr != L._tail) and (num != ind):
        curr = curr._next
        num = num + 1

    # get the two first letters of the first student's name
    begin = curr._element[0:2]
    # improve the result string
    result = result + begin.upper() + '-'
    # continue to check the list
    while(curr._next != L._tail) and (num != goal):
        curr = curr._next
        num = num + 1

    # get the two first letters of the last student's name
    end = curr._element[0:2]
    # complete the result string
    result = result + end.upper()

    # return the result string
    return result
