import time
from singly_linked_list import LinkedList

n=1000000

l = []
ll = LinkedList()

start_time = time.time()
for i in range(n):
    ll.add_to_tail(i) # O(1)
end_time= time.time()
print(f"Add to List took {end_time - start_time} seconds")

start_time = time.time()
for i in range(n):
    l.append(i) # O(1)
end_time= time.time()
print(f"Add to Linked List took {end_time - start_time} seconds")

start_time = time.time()
for i in range(n):
    l.pop(0)
end_time= time.time()
print(f"List pop from front took {end_time - start_time} seconds")

start_time = time.time()
for i in range(n):
    ll.remove_head()
end_time = time.time()
print(f"Linked List remove from front took {end_time - start_time} seconds")