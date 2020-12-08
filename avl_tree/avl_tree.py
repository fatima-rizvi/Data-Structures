"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the max depth
    """
    def max_depth(self):
        if not self:
            return 0
        left_depth = -1
        right_depth = -1
        if self.node.left:
            left_depth = self.node.left.max_depth() #Recursion
        if self.node.right:
            right_depth = self.node.right.max_depth()
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        if not self.node:
            return 0
        self.height = self.max_depth()

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        balance = self.balance
        if self.node.right and self.node.left:
            balance = self.node.left.max_depth() - self.node.right.max_depth()
        elif self.node.left and not self.node.right:
            balance = self.node.left.max_depth()
        elif self.node.right and not self.node.left:
            balance = 0 - self.node.right.max_depth()
        
        self.balance = balance

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):  #This was on the GCA :D
        if not self.node:
            return
        self.node.right = self.node
        self.node = self.node.left  #We only need to change the two because its like we're rotating them on a point, not changing all three 

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        if not self.node:
            return
        self.node.left = self.node
        self.node = self.node.right

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        tree_height = self.max_depth()
        if tree_height > 1 and self.node.key < self.node.left.node.key:
            self.right_rotate() # The value to the left needs to be smaller
        elif tree_height < -1 and self.node.key > self.node.right.node.key:
            self.left_rotate()
        elif tree_height > 1 and self.node.key > self.node.left.node.key:
            self.node.left.left_rotate()
            self.right_rotate
        elif tree_height < -1 and self.node.key < self.node.right.node.key:
            self.node.right.right_rotate()
            self.left_rotate()

        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if self.node:
            if key < self.node.key:
                if not self.node.left:
                    self.node.left = AVLTree(Node(key))
                else:
                    self.node.left.insert(key)
            else:
                if not self.node.right:
                    self.node.right = AVLTree(Node(key))
                else:
                    self.node.right.insert(key)
        else:
            self.node = Node(key)