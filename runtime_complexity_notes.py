# Runtime complexity

# This worked but wasn't the most appropriate way
# Using a wrench to hammer in a nail
commands = ['n', 's', 'w', 'e']

# Better way to do it would be a dictionary
# or a set
commands = set()


# How do we measure/objectivy efficiency anyway? 
# What tells us the list is less efficient?
# Answer: runtime complexity
# Runtime complexity is a way to objectively measure
# and compare the efficiency of two algorithms/approaches/strategies

# Complexity classes:
# Constant time: The efficiency of the code does not depend
# on the size of the input.
# Linear time: The efficiency does depend on the size
# of the input.

commands = ['n', 's', 'w', 'e']

# Constant Time
commands[3] # Doesn't matter how many elements are in the list
# If there are 1,000 elements and we do command[3], it goes
# As fast as if we had 4 elements in the list.
# The size of the input has no bearing on the efficiency of 
# this operation.

# Linear Time
# Grows 1:1 as the size of the input increases.
for command in commands: # but the for loop makes it linear
    print(command) # the print function is O(1), so this
                    # line is constant
    for _ in commands:
        # O(n) * O(n) which is O(n^2)
for _ in commands:
    # this would be O(n) + O(n) since its two for loops
    # happening after each other, not a for loop being executed
    # every time the other for loop runs
    # It's O(2*n) ~ O(n) -> allows us to drop constants because
    # it only care about the dominating factor for how something
    # grows

    # O(3n^2 + 3n + 4), Big O only cares about the n^2 because
    # it has the biggest effect on growth. Would simplify to
    # O(n^2). It's not real math. It's pretty hand-wavey.

# The size of the input has direct bearing on the efficiency
# of this operation b/c when the input size is bigger there
# are more things to run through the for loop.

selection = input()
# In the worst case, we'd have to iterate over every element
# in the list to find what we're looking for.
if selection in commands: 
    # If this is a valid command, perform user's command
    # Under the hood, this is a for loop so it's
    # a linear operation.

# Constant < Linear

# What's being compared is how quickly the efficiency grows
# as a result of the input size. In constant, growth is zero.
# In linear it's 1:1. If there's 1,000 items, there's 1,000
# for loop iterations. 

"""
        |     /
        |    /
 input  |   /- linear time
  size  |--/------------------- constant time
        | /
        |/
        ----------------------
        number of operations
"""

# Big O Notation
# O(1) Constant time: The efficiency does not depend on the
# size of the input, so that's O of 1
# Examples, indexing into a list
# Accessing value via it's key in a dict

# O(n) Linear time: The efficiency does depend on the size 
# of the input. n because it grows in relation to input
# size increase.
# Examples, iterating over elements in a list.

# Big O always looks at the worst-case scenario.


# Lists allow us to:
# 1. Store things in sequential order
# 2. Allow us to index to fetch particular elements by index.

# Linked Lists:
# 1. Store things in sequential order
# But don't allow you to index.

# Arrays are like a bookshelf where you can stack things 
# next to each other. But not linked lists!

list1 = [5, 7, 13, 18, 22, 3]

#Linked lists stores everything in its own node instead.
# Node is a class with a value:
class Node:
    def __init__(self, value, next_node=None):
        # the value that the node is holding
        self.value = value
        # reference to the next node in the linked list
        self.next_node = next_node

    def get_value(self):
    # method to get the value of the node
        return self.value

    def get_next(self):
    # method to get the node's next node
        return self.next_node

    def set_next(self, new_next):
    # method to update the next node's value
        self.next_mode = new_next

class LinkedList:
    # Will hold on to head node and tail node
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self):
        # wrap the value in a node
        new_node = Node(value)
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else: 
        # otherwise, the list has at least one node.
            self.tail.set_next(new_node)
            # update the last node's 'next_node' to new node
            self.tail = new_node
            # update 'self.tail' to point to new node just added

    def remove_tail(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        
        # check if the linked list has only one node
        if self.head == self.tail:
            # store the node we're going to remove's value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        
        # otherwise, the linked list has more than one Node
        # have to go back to the head because it's singly-linked
        # and work our way to second to last node
        
        else:
            # need to store Node's value in a variable so we can return it
            val = self.tail.get_value()
            # need to set 'self.tail' to second to last Node
            # by traversing the linked list from head
            # init another reference to keep track of where we
            # are in the linked list as we're iterating.
            current = self.head
            # keep iterating until the node after current is the tail
            # want to get to node whose next is the tail
            while current.get_next() != self.tail:
                # keep iterating
                current = current.get_next()
            
            # set 'self.tail' to 'current:'
            self.tail = current
            # set the new tail's 'next_node' to None
            self.tail.set_next(None)
            return val

    def remove_head(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
        # store the old head's value we need to return
        val = self.head.get_value()
        # set 'self.head' to the old head's 'next_node'
        self.head = self.head.get_next()
        # return the old head's value
        return val

# This approach sucks
# ll = Node(5)
# ll.set_next(Node(7))
# ll.next_node.set_next(Node(18))
# ll.next_node.next_node.set_next(Node(22))
# ll.next_node.next_node.next_node.set_next(Node(3))

# This approach is better
# ll.add_to_end(7)
# ll.add_to_end(18)
# ll.add_to_end(22)

ll=LinkedList() #makes head and tail both pointint to none
ll.add_to_tail(5)

# Stacks: Last In, First Out
# Like a stack of dishes, build from bottom up
# remove from top down using push and pop methods

# push(3)
# push(7)
# push(16)

# pop() -> removes 16
# pop() -> removes 7
# pop() -> removes 3

# Queues: First In, First Out
# The first person in a line is the first to leave
# enqueue and dequeue instead of push and pop

# enqueue(3)
# enqueue(7)
# enqueue(16)
# enqueue(4)

# dequeue() -> removes 3
# dequeue() -> removes 7
# dequeue() -> removes 16
# dequeue() -> removes 4
