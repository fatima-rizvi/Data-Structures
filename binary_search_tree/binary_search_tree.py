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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #Imagine there's a root of 10, we're doing recursion (which is where we call the function inside of itself. Crazy loops)
        #Below this, we're going down the tree and checking the values to see where to place this value
        if value < self.value: #If it's less, we're going to keep going down the left side. The smaller values are always to the left.
            if self.left: #Check if this exists
                self.left.insert(value) #This is the recursion
            else:
                self.left = BSTNode(value)
        else:   #If it's greater than OR EQUAL TO, we go down the right. 
            if self.right:  #Check if this exists
                self.right.insert(value) #This is the recursion
            else:   #If it's equal to, it'll go to here
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not

    # Recursion is kinda like a while loop
    # Recursion should always be moving towards the base case
    # TK code for contains
    def contains(self, target):
        if self.value == target:    # Base case: this should kill the recursion. It's like an exit condition of a while loop.
            return True
        elif target < self.value:   # Left side of the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)   # Recursion
        else:                       # Right side of the tree
            if self.right is None:
                return False
            else:
                return self.right.contains(target)  # Recursion

    # Return the maximum value found in the tree
    def get_max(self):
        # max_value = None # Can also set it to the first value in the tree, but None accounts for the tree being empty. Can also add that condition later
        # if max_value < self.value:
        #     max_value = self.value
        # The stuff above will not work if we use recursion

        # Recursion version
        # max_value = self.value                  # Starting at the first value
        # if max_value is not None:               # If the value is not none, if the value is actually there
        #     if self.right is None:              # If there is no right value, then this is the max value (since there are larger values to the right)
        #         return max_value                # Since it has to be the largest, we return it
        #     else:                               # If there is a value to the right
        #         return self.right.get_max()     # Recursion: Running the function again since we haven't found the max value
        # else:                                   # If there's nothing in the tree
        #     return None                         # Return None

        # While loop version
        current_node = self                     # Create a variable called current_node and set it equal to self (the current node)
        if current_node is None:                # If current_node is None, the tree is empty (edge case)
            return None                         # So we return None and stop the function. If we didn't, the last two lines would break the function

                                                # when current_node.right is none, the while loop will not run again
        while current_node.right:               # If there is something to the right of the current node (so something larger), the while loop will run
            current_node = current_node.right   # Set current_node to be the node to the right (the larger node)

        max_value = current_node.value          # Once we've broken out of the while loop, the current_node must be the max. Store its value in max_value
        return max_value                        # Return the max_value

        # Note: In this case, recursion didn't really save us any time or lines of code. Both are about the same length. Normally recursion is shorter.

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  
