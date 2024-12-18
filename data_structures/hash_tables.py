# in hash table, we store data and hash it and store them in a particular position
# the hastable is contructed oin top of linked list
# it has a hash function to contruct hash set and hash maps

class DoublyLinkedList:
    def __init__(self, val, prev = None, next = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

def createDLL(array : list):
    initial_pos = 0
    head = DoublyLinkedList(array[initial_pos])    
    curr = head
    current_index = 0
    while curr:
        if current_index == 0:
            curr.next = DoublyLinkedList(array[current_index + 1])

        elif current_index > 0 and current_index < len(array) - 1:
            curr.prev = DoublyLinkedList(array[current_index  - 1])
            curr.next = DoublyLinkedList(array[current_index + 1])

        elif current_index == (len(array) - 1):
            curr.prev = DoublyLinkedList(array[current_index  - 1])
        
        current_index += 1

        return curr

def display_dll(head : DoublyLinkedList):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
        
    print(" <-> ".join(elements))


array = [1, 2, 3, 4, 5]
dll = createDLL(array)
display_dll(dll)

# uptill now we created the doubly linked lists for performing the has table functions

# in hashmap there is a problem called collision where the has position matches with two values created collision to store data in that position indez

# hashable data -> int, tuple, string as they are mutable

# there are many methods: 
# linear probing where the has function creates a position and if that position is filled it looks for next index and find if it's empty it gets filled. here things can get worse searching for a similar data index in a lookup scenario.

# hash set
s = set()

# adding data into the set
s.add(1)
s.add(2)
s.add(3)

# lookup operation
if 1 in s:
    print(True)

# remove operations
s.remove(3)
print(s)

non_unqiue_strings = 'aaaaaaaaabbbbbbbbbbbbbbbbcccccccccccccdddddd'
unique_set = set(non_unqiue_strings)
print(unique_set)

# hashmaps -> dictionary
d = {
    'name' : 'Emmanuel A',
    'age' : 21,
    'Gender' : 'M',
}

# add
d['address'] = '197, c, P.S street, Ayanavaram, Chennai - 23.'
print(d)

# lookup
if d['Gender'] == 'M':
    print(True)

# loop through -> O(n)
for key, val in d.items():
    print("{0} || {1}".format(key, val))

from collections import Counter

counts = Counter(non_unqiue_strings)
print(counts)