# it has the Last In First Out Data structure -> LIFO
# we can use dynamic array or doubly linked list to build it

# operations: 
# 1. adding -> O(1)
# 2. delete -> delete the last element O(1)
# 3. peek -> peek the last element O(1)
# 4. isempty() -> find out if it is empty

stack = []

# add
stack.append(3)
stack.append(5)
stack.append(10)
stack.append(12)
print(stack)

# remove last item
last_items = stack.pop()
print(last_items)

# lookup last item -> peek
print(stack[-1])