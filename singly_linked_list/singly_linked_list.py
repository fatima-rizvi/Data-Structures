# A singly linked list is kind of shaped like a list, but nothing has an index list. It has a head, which has an attribute pointing to the next item in the list and so on until the end. You can only go forward in this list. Items do not know what came before it, only what comes directly after.
#They're pretty fast at certain things

class Node: 
    def __init__(self, value):  # We don't pass in a next value because each item may be the last and we don't know what might come next
        self.value = value
        self.next = None    

    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None    # First node in the linked list. These are pointers 
        self.tail = None    # Last node in the linked list. These are pointers

    # Notes of Linked Lists:
    # Each node has a value and a next.
    # The "next" is pointing to the next item's memory location, bc the cool thing about a linked list is that the items aren't stored next to each other. Each node can be stored anywhere. Important for big O notation.
    # Unlike regular lists, where all of the items are stored next to each other so the computer needs to find a location large enough to hold the entire list together. And when the list becomes to large for the spot it's stored in, the computer needs to go copy the whole list to somewhere else. This doesn't happen, but it makes list operations take just a little more time 
    # Linked list just need one spot per node
    # A singly linked list is where the "arrow" only points in one direction. Each node only points to the head of the one after it. We'll learn about doubly linked lists later
    
    # Most of the time, like in our hw assignments, the tail of the linked list isn't tracked, so we'd need to find it ourselves.
    # Typically, to move along a linked list (esp one that doesn't track the trail), you would create a for loop to go through each node one by one. If the current node doesn't have the value you're looking for, then you move the the next node until you find the value. If you're looking for the tail, you look for  when th enext of the current node is None.


    def add_to_tail(self, value):
        new_node = Node(value)
        # If the list is empty/doesn't exist (edge case). How would we know if it's empty? If self.head is None.
        if self.head is None: #The "is" operator compares the identity of two objects while "==" compares the value of two objects. None has no location in memory, so I don't think we can use == but don't quote me on that.
            self.head = new_node    # The new node will be the head
            self.tail = new_node    # And since there is only one node the tail will also point here
            return #You could use "break" here instead to get out of the if statement (more useful for loops), but it would still continue to the next line so maybe don't. Return will end the function
        # Since we tracked the tail, we just need to make a node come after the tail (next) and then move the pointer of the tail to the new node
        self.tail.next = new_node #
        # Now we need to reassign the tail pointer bc it's currently pointing at the old tail.
        self.tail = new_node # Could also be assigned to the value of self.tail.next, it's the same thing.

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






        