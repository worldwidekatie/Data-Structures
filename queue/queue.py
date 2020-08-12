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

# Regular List - Passed Tests
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []      

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         return self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) > 0:
#             return self.storage.pop(0)
#         else:
#             return None


# From Linked List
class Node:
    def __init__(self, value, next_node=None):
        # the value that the node is holding 
        self.value = value 
        # reference to the next node in the linked list
        self.next_node = next_node

    # method to get the value of the node 
    def get_value(self):
        return self.value

    # method to get the node's `next_node`
    def get_next(self):
        return self.next_node

    # method to update the node's `next_node` to the input node 
    def set_next(self, new_next):
        self.next_node = new_next

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        # wrap the value in a Node
        new_node = Node(value)
        # check if the Linked List is empty 
        if self.head is None and self.tail is None:
            # set head and tail to the new node 
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node 
        else:
            # update the last node's `next_node` to the new node 
            self.tail.set_next(new_node)
            # update `self.tail` to point the new node we just added 
            self.tail = new_node
        
        self.size +=1

    def dequeue(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            self.size -=1
            return val
        else:
            # store the old head's value we need to return
            val = self.head.get_value()
            # set 'self.head' to the old head's 'next_node'
            self.head = self.head.get_next()
            self.size -=1
            # return the old head's value
            return val
