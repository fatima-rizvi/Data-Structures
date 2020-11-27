#Import linked list
from singly_linked_list import LinkedList

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

#Think of a stack of pancakes. You put things on the top and take them off the top
    #If you use an array, you add to the beginning and remove from the beginning. Just pull and push from the same end, whether or not you pick the beginning or ending. The side you pick, front or back or top or bottom etc., doesn't really matter, just keep adding and removing from the same end.
    #You can also think of a stack on envelopes
#In a queue, think of a shopping queue. People join from the end and leave from the front
    #You can also think of a airport security line

# Side note: A multi-dimentional list is an array of arrays, so like getting an object full of objects back from an API
# [ [],[],[],[] ] Like nesting list within a list

#THIS IS HOW TO DO IT WITH A LIST
# class Stack:
#     def __init__(self): #, storage = [] you could also add this and do self.storage = storage on line 23. Better to not do that though so that there's less for your brain to think about. Keep it simple.
#         self.size = 0
#         self.storage = [] #Can be called inventory, etc. Doesn't need to be called storage. Initialize an an empty list

#     def __len__(self): #You could track the length of a linked list, you just have to create that functionality
#         return len(self.storage) #This is how to do it as an list

#     def push(self, value):
#         #PICK ONE OPTION BELOW, and then pick the CORRESPONDING option in the pop method because this is a STACK. BE CONSISTENT.
#         #return self.storage.append(value) #This adds to the end (tail)
#         return self.storage.insert(0, value) #This adds to the start (head). Like the top of a stack of pancakes.

#     def pop(self):
#         if len(self.storage) == 0:
#             return
#         # removed = self.storage[-1] #last item
#         # del self.storage[-1] #Remove from the end
#         removed = self.storage[0] #first item
#         del self.storage[0]  #Removes from the start
#         return removed

#Side note: Alt and up and down arrows to move stuff up and down. Add ctrl to copy and paste

#THIS IS HOW TO DO IT WITH A LINKED LIST
class Stack:
    def __init__(self): 
        self.size = 0
        

    def __len__(self): 
        pass

    def push(self, value):
        pass

    def pop(self):
        pass