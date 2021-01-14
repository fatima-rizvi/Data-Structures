# import sys
# sys.path.append('../singly_linked_list')
# from singly_linked_list import LinkedList

# import sys
# sys.path.append('../queue')
# from queue import Queue

# import sys
# sys.path.append('../stack')
# from stack import Stack

# A singly linked list is kind of shaped like a list, but nothing has an index list. It has a head, which has an attribute pointing to the next item in the list and so on until the end. You can only go forward in this list. Items do not know what came before it, only what comes directly after.
#They're pretty fast at certain things

# Imports were confusing so we just copy and pasted
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None: #The "is" operator compares the identity of two objects while "==" compares the value of two objects
            self.head = new_node
            self.tail = new_node
            return #You could use "break" here instead, but it would still continue to line 20 so maybe don't. Return will end the function
        self.tail.next = new_node
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)  #Created the new_node
        if self.head is None:   #Just in case there isn't already a head, meaning the list is empty
            self.head = new_node
            self.tail = new_node
            return
        old_head = self.head    #This way, the old head doesn't disappear and we can link it to the new one
        self.head = new_node    #Assigning the new_node to the head
        self.head.next = old_head #Reassigning the old head to the next of the new one

    def remove_head(self):
        if self.head is None: #There's nothing to remove if the list is empty, which it is if head is empty
            return
        data = self.head.get_value()
        self.head = self.head.next
        return data

    def remove_tail(self):
        data = self.tail.get_value()
        cursor = self.head  #Can also be pointer. Start at the head
        # Using cursor.next.next so that when the next item of our next item is none, we know that our item is the item before the tail
        while cursor.next.next is not None:   #We don't know how long the list is, hence a while loop
            cursor = cursor.next    #Move the cursor to the next one
        self.tail = cursor   #Set linked list's tail to the cursor
        self.tail.next = None   #Get rid of the connection/arrow to the old tail
        return data

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1  # self.size = self.size + 1 (same thing)
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return
        self.size -= 1 # self.size = self.size - 1 (same thing)
        return self.storage.remove_head()

class Stack:
    def __init__(self): 
        self.size = 0 #Keep track of the length. You could do this in the linked list class
        self.storage = LinkedList()        

    def __len__(self): 
        return self.size

    def push(self, value):
        self.size += 1 #Keep track of the length
        return self.storage.add_to_head(value) #We've chosen to add/remove from the start

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1 #Keep track of the length
        return self.storage.remove_head()
        

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
        # Recursion version
        # max_value = self.value                  # Starting at the first value
        # if max_value is not None:               # If the value is not none, if the value is actually there
        #     if self.right is None:              # If there is no right value, then this is the max value (since there are larger values to the right)
        #         return max_value                # Since it has to be the largest, we return it
        #     else:                               # If there is a value to the right
        #         return self.right.get_max()     # Recursion: Running the function again since we haven't found the max value
        # else:                                   # If there's nothing in the tree
        #     return None                         # Return None

        # max_value = None # Can also set it to the first value in the tree, but None accounts for the tree being empty. Can also add that condition later
        # if max_value < self.value:
        #     max_value = self.value
        # # The stuff above will not work if we use recursion

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

    # Ava
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self:
            return
        fn(self.value)
        if self.left:
            self.left.for_each(fn)    #Recursion
        if self.right:
            self.right.for_each(fn)   #Recursion
    # def for_each(self, fn):
    #     if not self:
    #         return
    #     fn(self.value)
    #     if self.left:
    #         self.for_each(self.left, fn)    #Recursion
    #     if self.right:
    #         self.for_each(self.right, fn)   #Recursion
        

    # Part 2 -----------------------

    # Josh
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # def in_order_helper(self, node):
    #     if node is None:
    #         return
    #     bst.in_order_helper(node.left)
    #     print(node.value)
    #     bst.in_order_helper(node.right)

    # def in_order_print(self):
    #     # result = []
    #     bst.in_order_helper(self)
    #     # return result    

    # Ava
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()     #Recursion is your friends :')
        print(self)
        if self.right:
            self.right.in_order_print()   #Recursion


    
    # Mine and Doc's
    # def bft_print(self):
    #     current_level = [self]
    #     while current_level:
    #         next_level = list()
    #         for node in current_level:
    #             print(node.value)
    #             if node.left:
    #                 next_level.append(node.left)
    #             if node.right:
    #                 next_level.append(node.right)
    #         print()
    #         current_level = next_level
        
    
    # Ava
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal (iterative, no recursion :'( )
    def bft_print(self):
        q = Queue()
        q.enqueue(self)
        while q.size != 0:
            current = q.dequeue()
            print(current.value)
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal (iterative, so we'll use a queue and stack)

    # Ava
    def dft_print(self):
        s = Stack()
        s.push(self)
        while s.size != 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)
    

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Josh
    # Print Pre-order recursive DFT
    # def pre_order_helper(self, node):
    #     if node is None:
    #         return
    #     print(node.value)
    #     bst.pre_order_helper(node.left)
    #     bst.pre_order_helper(node.right)

    # def pre_order_dft(self):
    #     # result = []
    #     bst.pre_order_helper(self)
    #     # return result  

    #Ava's solution
    def pre_order_dft(self):  
        if self:
            print(self.value)   #No need to return, just printing values
            if self.left:
                self.left.pre_order_dft()
            if self.right:
                self.right.pre_order_dft()
            
    # Josh
    # Print Post-order recursive DFT
    # def post_order_helper(self, node):
    #     if node is None:
    #         return
    #     bst.post_order_helper(node.left)
    #     bst.post_order_helper(node.right)
    #     print(node.value)

    # def post_order_dft(self):
    #     # result = []
    #     bst.post_order_helper(self)
    #     # return result

    # Ava :)
    def post_order_dft(self):
        if self:
            if self.left:
                self.left.post_order_dft()
            if self.right:
                self.right.post_order_dft()
            print(self.value)

        
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
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
