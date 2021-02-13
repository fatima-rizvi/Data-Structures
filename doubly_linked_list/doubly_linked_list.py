"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
# Walk through whatever was pre built
class ListNode:
    def __init__(self, value, prev=None, next=None):    # Note: Explain what the defaults mean or how the node looks
        self.prev = prev
        self.value = value
        self.next = next
        
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0  # We could call length anything, it's just a variable that's been created

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):   # 1. Ask, what do we need to do to add to the head?
        new_node = ListNode(value)  # 2. Create a new node
        old_head = self.head        # 3. (Optional, but better for understanding) Store the old head node in a variable to keep track of it  
        new_node.next = old_head # 4. You only need new_node.next = self.head but this explains what's going on better
        
        # 9. Edge case: What if the list is empty? Does it change what we do? How?
        if self.head is None: # Since there was nothing in the list before this, this becomes the entire list
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return

        old_head.prev = new_node # 5. self.head.prev = new_node (same thing). By giving the old head a prev, it's no longer the head.
        # 6. BUT we still need to move the self.head pointer
        self.head = new_node # 7. Moves our pointer (head) to the "front". Head is just a variable we use for our computer to point to where we want to start.
        self.length += 1 # 8. Q: What do we need to do for our len function to work properly? A: increase length
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # 8. Q: What are the possible edge cases? A: Where list is empty or where there is only one item.
        if self.length == 0:    # 9
            return              # 10. Return by itself returns a None value

        value = self.head.value # 1. Let's grab the value of the node to return later. self.head returns the location of the node, not the value
        
        if self.length == 1:        # 11
            self.head = None #The list is empty now
            self.tail = None #The list is empty now
            self.length = 0
            return value

        # 2. Q: How do we want to go about removing the head?
        new_head = self.head.next   # 3. Grab the node that we'll want to be the new head and store it (to make things easier in our head)
        self.head = new_head     # 4. Set the head pointer to the new head. It's .prev still points to the old head
        self.head.prev = None # 5. Get rid of the pointer to the old head, so that nothing is still pointing at the old head
        self.length -= 1 # 6. Decrease the length

        return value    # 7. Return the value we grabbed for testing purposes
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return 

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return
        
        value = self.tail.value
        
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return value

        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1

        return value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            return

        if self.head is node:
            return
        
        if self.tail is node:
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
            self.add_to_head(node.value)
            return


        node.prev.next = node.next #Connect the node's next and previous nodes with each other
        node.next.prev = node.prev #Connect the node's next and previous nodes with each other
        self.length -= 1  #We didn't really add anything new, and this is needed because of the next line
        self.add_to_head(node.value) #use our built in method to add to head
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 0:
            return

        if self.tail is node:
            return

        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            self.add_to_tail(node.value)
            return

        node.prev.next = node.next
        node.next.prev = node.prev 
        self.length -= 1
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return

        self.length -= 1

        if self.head is node:
            self.head = node.next
            self.head.prev = None
            return

        if self.tail is node:
            self.tail = node.prev
            self.tail.next = None
            return

        node.prev.next = node.next
        node.next.prev = node.prev 
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value 
        pointer = self.head 

        while pointer is not None:
            if max_value < pointer.value:
                max_value = pointer.value   # Can compare letters, z > a, tuples, 
            
            pointer = pointer.next 

        return max_value