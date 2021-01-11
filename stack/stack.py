#Import linked list
#Folder name.file name, thing to import
# from singly_linked_list.singly_linked_list import LinkedList  # try this import too

# This might be a pain in the butt bc they're in different directories
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'singly_linked_list'))
from singly_linked_list import LinkedList   # see if this line alone works, but doubtful. Copy and paste the import above. I think pycharm makes it easier.

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
as the underlying storage structure.
Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
implementing a Stack?
"""
# Note: Even though we're going To build a class, you can use a list as a stack or queue

# First chunk of explanation
    #Think of a stack of pancakes. You put things on the top and take them off the top
        #If you use an array, you add to the beginning and remove from the beginning. Just pull and push from the same end, whether or not you pick the beginning or ending. The side you pick, front or back or top or bottom etc., doesn't really matter, just keep adding and removing from the same end. 
        # Like, whatever "end" you pick, your adding to the top of the stack of pancakes and removing from the top of the stack of pancakes.
        #You can also think of a stack on envelopes
    #In a queue, think of a shopping queue. People join from the end and leave from the front
        #You can also think of a airport security line

# Side note: A multi-dimentional list is an array of arrays, so like getting an object full of objects back from an API
# [ [],[],[],[] ] Like nesting list within a list. We'll use something like this for graphs later, I think
# Again, remember that python doesn't have arrays (outside of NumPy(?)), but lists are basically like arrays

# 1. DIRECTIONS: First we're going to make a stack with an array, then with the singly linked list we created

# THIS IS HOW TO DO IT WITH A LIST
class Stack:
    def __init__(self): # 4. , storage = [] you could also add this as a parameter and do self.storage = storage for the attribute. Better to not do that though so that there's less for your brain to think about. Keep it simple.
        self.size = 0
        self.storage = [] # 3. Can be called inventory, etc. Doesn't need to be called storage. Initialize an an empty list 

    def __len__(self): #1. Note: You could track the length of a linked list, you just have to create that functionality
        # 2. Basically, we'll want to return the length of the list, so we need to create a place to hold the list
        return len(self.storage) # 5. Q: How do we return the length of a list? What list do we want the length of? This is how to do it as a list
        # 6. Hop up to the side note above if you'd like

    def push(self, value):
        # 1. Two ways to do this, based on if you wan thtis stack to add and remove from the tail or the head
        # 4. PICK ONE OPTION BELOW, and then pick the CORRESPONDING option in the pop method because this is a STACK. BE CONSISTENT.
        #return self.storage.append(value) # 2. This adds to the end (tail)
        return self.storage.insert(0, value) # 3. This adds to the start (head). Like the top of a stack of pancakes.
        # 5. Note, we are returning them because the tests want us too

    def pop(self):
         # 10. Edge case: If there is nothing in the list
        if len(self.storage) == 0:  # 11
            return                  # 12
        # 1. Now, it would be nice to use the built in list's pop() method here, but because of the tests we are required to  name the function pop, so we have to find another way to do it. If we tried to use pop(), it won't work because we've overwritten it. 
        # 2. So we're going to use this key word called "del" that removes the item at the specified index but DOES NOT return it.
        # 3. If you want to remove from the tail of the list, use the two lines below
        # removed = self.storage[-1] # 4. last item. Store the item in another variable to be returned later for testing purposes
        # del self.storage[-1] # 5. Remove from the end. Use the del key word and negative indexing.
        # 6. If you want to remove from the head of the list, use the two lines below
        removed = self.storage[0] # # 7. first item. Store the item in another variable to be returned later for testing purposes
        del self.storage[0]  # 8. Removes from the start. Use the del key word
        return removed  # 9. Return the removed value

# Side note: Alt and up and down arrows to move stuff up and down. Add ctrl to those steps to copy and paste
# Also, shift + tab to un-tab

#THIS IS HOW TO DO IT WITH A LINKED LIST (the one that we made)
# import the singly linked list
        
# class Stack:
#     def __init__(self): 
#         self.size = 0 # Keeps track of the length. Note: You could do this in the linked list class too by adding this attribute to keep track of its length.
#         self.storage = LinkedList() # 1. This time, we will create an instance of our linked list class

#     def __len__(self): 
#         return self.size    # 2. How will we track the length?

#     def push(self, value):  # 5. Now let's work on this
#         self.size += 1 # 3. We'll need to update self.size everytime we push or pop. Keep track of the length
#         return self.storage.add_to_head(value) # 6. We've chosen to add/remove from the start to make our lives easier
#         # We're returning it for testing purposes

#     def pop(self):  # 7. Now lets work on this. Q: How would we pop it?
#         # 9. Edge case: What if the list is empty? What do we want to do and how?
#         if self.size == 0:
#             return  # We need to return here because 1) there's nothing to remove and 2) and size cannot be less than 0
#         self.size -= 1 # 4. We'll need to update self.size everytime we push or pop. Keep track of the length
#         return self.storage.remove_head()   # 8. Remove from head using the LinkedList methods
#         # We're returning it for testing purposes