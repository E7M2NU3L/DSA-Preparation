# it is the First in First Out Data structure -> FIFO
# it can be built with doubly linked list

# operations
# 1. Enqueve -> add new item to the queve
# 2. Dequeve -> pop last item from the queve

from collections import deque

queve = deque()

# adding
queve.append(1)
queve.append(2)
queve.append(3)
queve.append(4)
print(queve)

# deleting
first_out_item = queve.popleft()
print(first_out_item)

# peeking items
print(queve[0], queve[-1])