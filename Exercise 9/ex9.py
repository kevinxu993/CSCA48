class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.d = 0

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, d):
        ''' (BTNode, int) -> None
        The method will set the add the node's .d from provided value.
        '''
        # set current depth
        self.d = d
        # if left child is not None, then set it with depth+1
        if self.left is not None:
            self.left.set_depth(d+1)
        # if right child is not None, then set it with depth+1
        if self.right is not None:
            self.right.set_depth(d+1)

    def leaves_and_internals(self, is_root=True):
        """(BTNode, bool) -> tuple
        Return a tuple with two sets. The first set is vlues of the
        leaves and the secound is the set of the internal node
        Leaves are node that don't have child, and internal are the
        rest except the root node
        """
        # Create the tuple with two set
        ret_tuple = (set(), set())

        # If it is a leaf noed
        if(self.right is None and self.left is None):
            ret_tuple[0].add(self.value)

        # If it is not a leaf node
        else:
            # Make sure it is not head (internals)
            if(not is_root):
                ret_tuple[1].add(self.value)

            # If there is a right node
            if(self.right is not None):
                right_tuple = self.right.leaves_and_internals(False)
                ret_tuple[1].update(right_tuple[1])
                ret_tuple[0].update(right_tuple[0])

            # If there is a left node
            if(self.left is not None):
                left_tuple = self.left.leaves_and_internals(False)
                ret_tuple[1].update(left_tuple[1])
                ret_tuple[0].update(left_tuple[0])

        return ret_tuple

    def sum_to_deepest(self):
            ''' (BTNode) -> int
            The method will return the sum of the deepest
            tree by calling helper function.
            '''
            return self.sum_helper()[0]

    def sum_helper(self, d=0):
        ''' (BTNode, int) -> [int, int]
        The method is the helper function for sum_to_deepest.
        The function will return a list of sum and depth.
        '''
        # if there is no child, return value and depth
        if self.left is None and self.right is None:
            return [self.value, d]
        # if there are two children
        elif self.left is not None and self.right is not None:
            # get the left and right child
            left = self.left.sum_helper(d+1)
            right = self.right.sum_helper(d+1)
            # if left d is greater
            if left[1] > right[1]:
                return [left[0]+self.value, left[1]]
            # if right d is greater
            elif left[1] < right[1]:
                return [right[0]+self.value, right[1]]
            # if depth are equal
            else:
                # return the value which is greater
                return [left[0]+self.value, left[1]] if left[0] > right[0]\
                       else [right[0]+self.value, right[1]]
        # if it just has one child
        else:
            # recall this method to get the child value and d
            child = self.left.sum_helper(d+1) if self.left is not None\
                else self.right.sum_helper(d+1)
            return [child[0]+self.value, child[1]]

if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))
    print(my_tree)
    print(my_tree.leaves_and_internals())
    print(my_tree.sum_to_deepest())
