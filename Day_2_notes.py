# Linked Lists vs Arrays

# contiguously means packed in memory right next
# to each other.

# Linked lists exhibit a linear runtime because
# you might have to traverse through the whole
# list to access an item.

# What are linked lists even good for?
# For lists, removing an item creates a hole
# that has to be filled by shifting everything over.
# Removing an element that's not the last element
# in the array is worst-case O(n).

# But linked lists don't have such a cost for 
# removing elements. They do have an upside!
# I was skeptical. 

# If a node is in memory but not referenced,
# memory thinks it's trash and throws it away.
# This is reference-counting garbage collection

# Runtime for removing an element (when we already
# have access to the previous node) in a linked
# list is O(1)

# Removing from front of array is worst-case O(n)
# Removing from back of array is worse-case O(1)
# Inserting to front of array is worst-case O(n)
# Inserting to back of array is worst-case O(1)


"""Doubly Linked Lists"""



