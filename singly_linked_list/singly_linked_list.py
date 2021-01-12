# A singly linked list is kind of shaped like a list, but nothing has an index list. It has a head, which has an attribute pointing to the next item in the list and so on until the end. You can only go forward in this list. Items do not know what came before it, only what comes directly after.
#They're pretty fast at certain things

class Node: 
    def __init__(self, value):  # We don't pass in a next value because each item may be the last and we don't know what might come next
        self.value = value      # Each node in a linked list has a value and a next 
        self.next = None        # This points to the next node in the list

    def get_value(self):        # THIS GETS MADE LATER, when we make the remove_head and remove)tail methods
        return self.value       # This is really simple, we just need to be able to return the value on any node. Honestly, I'm not sure if this was necessary, we might've just been able to return the node.value in those methods buuuuuut this is good practice I guess.

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
        new_node = Node(value)  # 1
        # 6. Edge case: If the list is empty/doesn't exist. Q: How would we know if it's empty? Ans: If self.head is None.
        if self.head is None: # 7. The "is" operator compares the identity of two objects while "==" compares the value of two objects. None has no location in memory, so I don't think we can use == but don't quote me on that.
            self.head = new_node    # 8. The new node will be the head
            self.tail = new_node    # 9. And since there is only one node the tail will also point here
            return # 10. You could use "break" here instead to get out of the if statement (more useful for loops), but it would still continue to the next line so maybe don't. Return will end the function
        # 2. Since we tracked the tail, we just need to make a node come after the tail (next) and then move the pointer of the tail to the new node
        self.tail.next = new_node # 3. Reassign the the next of the tail to the new node
        # 4. Now we need to reassign the tail pointer bc it's currently pointing at the old tail.
        self.tail = new_node # 5. Could also be assigned to the value of self.tail.next, it's the same thing.

    def add_to_head(self, value):
        new_node = Node(value)  # 1. Created the new_node
        # Edge case of if there is no list. It's easier to go through the the code to solve the majority of cases before we try to solve the edge cases
        if self.head is None:   #Just in case there isn't already a head, meaning the list is empty
            self.head = new_node    # Reassign the pointers just like we did before
            self.tail = new_node    # Reassign
            return                  # End the function here
        # 2. Slight problem here, a difference compared to adding_to_tail. If we try to immediately reassign self.head or self.head.next, we lose whatever nodes that we originally there (unlike how self.tail.next was None, self.head has a value). 
        # 3. That's because in python, and possibly in computers/programming languages in general, once there is nothing pointing to a memory location, whatever data is at that location virtually ceases to exist and that location is seen as "empty", so the computer can fill it with new data.
        # 4. So, if a node doesn't have anything pointing at it, it basically no longer exists. How do we get around this problem?
        old_head = self.head    # 5. Create something to hold the old head. This way, the old head doesn't disappear and we can link it to the new one
        self.head = new_node    # 6. Assigning the new_node to the head of the linked list
        self.head.next = old_head # 7. Reassigning the old head to the next of the new one

    # For session purposes, pause here and define other necessary methods, but only fill out "pass" in them. Then run the test file with this:
    # python -m singly_linked_list
    # Note, these tests aren't super well written out for us to read, but for the most part they let us know if we built our functions correctly. The ones on code signal are nicer

    def remove_head(self):  # 1. Ask if we need to pass anything in, then ask how they would go about removing the head. 
        # We'll need to reassign self.head to self.head.next
        if self.head is None: # 3. There's nothing to remove if the list is empty, which it is if head is empty
            return  # 4

        data = self.head.get_value() # 7. Write this AFTER writing the main and edge cases. The tests want us to return the value we are removing, we'll need to build the get value method into the node class. Show that to the group. This needs to be under the first edge case, because we can't get the value on a none type. 

        # 5. Q: What if there is only one node in the list? A: Then we just set head and tail to None to effectively delete the list
        if self.head.next is None:
            self.head = None
            self.tail = None
            return data # 6

        self.head = self.head.next  # 2. Reassign the head pointer to self.next.head, effectively wiping the old head from memory.
        return data # 8

    def remove_tail(self):
        # 1. Funky thing here, we don't have anything pointing to the node before the tail, so how do we find it?
        # 2. We'll need to create loop to find it. Which kind? A while loop.

        # 13. Edge case: What if the list is empty? Then just end the function.
        if self.head is None:
            return

        data = self.tail.get_value() # 12. We still need to return the value of the removed tail for the tests, so let's grab it
        # 3. We also need a cursor/pointer to keep track of the node we're on
        cursor = self.head  # 4. Can also be pointer. Start at the head
        # 6. Using cursor.next.next so that when the next item of our next item is none (use diagram), we know that our item is the item before the tail

        # 14. Edge case: What if the list is only one node long? Then we want to just effectively delete the whole list by resetting all pointers to None.
        if self.head.next is None:
            self.head = None
            self.tail = None
            return data

        while cursor.next.next is not None:   # 5. We don't know how long the list is, hence a while loop
            cursor = cursor.next    # 7. What do we do here if the cursor is not on the node we want (second to last)? Move the cursor to the next one. This loop will stop runnign once we reach the second to last node
        # 8. What do we do once we've reach the second to last node and exited the loop? What is our goal with our current node, our cursor?
        # 9. We want our current node to become the new tail, and we need to erase the old tail by getting rid of anything pointing to it. How?
        self.tail = cursor   # 10. We set linked list's tail to the cursor
        self.tail.next = None   # 11. Get rid of the connection/arrow to the old tail
        return data     # 13. Return the value

# Note: When teaching, make sure to print the node or something at some point so you can show what the node's momory location looks like, that way they know what that is if it ever pops up while programming.




        