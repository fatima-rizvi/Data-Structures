# import sys, os
# sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'singly_linked_list'))
# from singly_linked_list import LinkedList

import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList   # here's a shorter import that we probs could've used for stack.py :P

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# Using out LinkedList class (import)
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList() # 1. What do we want to set self.storage equal to? 
    
    def __len__(self):
        return self.size    # 2. How do we want to get the size of the list? 

    def enqueue(self, value):  # 3 # Means to add it to the queue (at the end, bc it's a queue)
        self.size += 1  # 5. self.size = self.size + 1 (same thing)
        self.storage.add_to_tail(value) # 4

    def dequeue(self):  # 6 # Means to remove it from the queue (from the head, bc it's a queue)
        if self.size == 0: # 9. Q: Is there an edge case? What is it and what do we do? what if there isn't anything in the list?
            return
        self.size -= 1 # 8 # self.size = self.size - 1 (same thing)
        return self.storage.remove_head() # 7 

# We're not going to do this with a regular list for time's sake, but you get the idea

# Check out the deck imports for queses from collections