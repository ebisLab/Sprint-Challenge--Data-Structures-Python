"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # checking if the incoming value is less than the current node value
        if value < self.value:  # we're comparing in insert to know which direction to go in
            # go left
            # signal to recurse again
            # or when to stop
            if not self.left:
                # we can park our value here
                self.left = BSTNode(value)
            else:
                # we cant park here
                # we still ned to go left, but we need to still keep looking
                self.left.insert(value)
        else:
            # go right
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)  # no need to return anything

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # When we start searching, self will be the root
        # compare the target against self
        #
        # criteria for returning fals: we know we need o go in one direction
        # but there's no children
        if target == self.value:  # we're comparing to stop our recursion. We might find our value right off the bat
            return True
        if target < self.value:
            # go left if left is a BSTnode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # we'll
        if not self.right:
            return self.value
        # otherswise, keep giong righ
        return self.right.get_max()
        # return None  # why not return self.right.get_max()

    def iterative_get_max(self):  # shows what recursion is doing under the hood
        current_max = self.value

        current = self  # current node we're on
        # traverse our structure
        while current is not None:
            if current.value > current_max:
                current_max = current.value
        # update our current_max variable if we see a larger value
            current = current.right
        return current_max

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # call the fn on the value at this node
        fn(self.value)

        # pass this function to the left child
        if self.left:
            self.left.for_each(fn)
        # pass this function to the right child
        if self.right:
            self.right.for_each(fn)
            # breadth first
    # Depth -first traversal follows LIFO orderdring of the tree elemenents

    # Depth -first traversal follows LIFO orderdring of the tree elemenents

    def iterative_for_each(self, fn):
        stack = []
        # add the root node if stack is empty
        stack.append(self)
        # loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            fn(current.value)


# Breadth --- first in firsto out ordering
# iteratively


    def breadth_first_for_each(self, fn):
        queue = deque()

        # add the root node if queue is empty
        queue.append(self)
        # loop so long as the queue still has elements
        while len(queue) > 0:
            current = queue.popleft()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)

            fn(current.value)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        # pass this function to the left child
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        # pass this function to the right child
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()

        # add the root node if queue is empty
        queue.append(node)  # replaced self with node

        # loop so long as the queue still has elements
        while len(queue) > 0:
            current = queue.popleft()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)

            # print
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        stack = []
        # add the root node if stack is empty
        stack.append(node)  # self -> node
        # loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            # print
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
# bst.dft_print(bst)
