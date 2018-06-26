from week6_heap import Heap


def merge_heap(h1, h2):
    '''(Heap, Heap) -> Heap
    Takes two heaps as input parameters and returns a heap that contains all
    the names in both Marzieh's and Nick's class.
    REQ: h1 and h2 are two heaps.
    '''
    while not h2.is_empty():
        h1.insert(h2.remove_last_node())

    return h1


def first_and_last(h):
    '''(Heap) -> (String, String)
    Takes a heap as an input parameter and returns a tuple containing the
    surname of the first and last student in alphabetical order.
    '''
    first = h.min()
    last = h.remove_last_node()
    while not h.is_empty():
        remove = h.remove_last_node()
        if remove > last:
            last = remove

    return (first, last)
