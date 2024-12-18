# linked list -> singly linked list and doubly linked list

# it has a node which contains a position and memory address
# 1 -> 2 -> 3 -> Null which is the end of the list

# it does about O(n) operation

# conventional method
class FindNumber:
    def __init__(self, array, number_of_find) -> None:
        self.array : list = array
        self.number_to_find : int = number_of_find
        self.pos = 0

    def find_the_number(self):
        while True:
            if self.pos >= len(self.array):
                print("the number is not in the list")
                break

            elif self.array[self.pos] == self.number_to_find:
                print('The number {0} is in position {1}'.format(self.number_to_find, self.pos))
                break

            self.pos += 1

number_to_find = 3
array = [1, 2, 3, 4, 5, 6]
find_number_intance = FindNumber(array, number_to_find)
find_number_intance.find_the_number()

# 

# method with linked list
class findNumberLL:
    def __init__(self, array, number_to_find) -> None:
        self.array = array
        self.number_to_find = number_to_find

    def find_the_number(self):
        curr = self.array
        while curr:
            if self.number_to_find == curr.val:
                print("The number: {0} is in the list".format(self.number_to_find))
                return True

            curr = curr.next

        print("the number is not in the list")
        return False

class SingleLinkedList:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)
    
# Creating the Single Linked List
head = SingleLinkedList(1)
A = SingleLinkedList(3)
B = SingleLinkedList(5)
C = SingleLinkedList(7)
D = SingleLinkedList(9)

head.next = A
A.next = B
B.next = C
C.next = D

# creating doubly linked list which has both prev and next information
class DoublyLinkedList:
    def __init__(self, val, prev = None, next = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)
    
DHead = DoublyLinkedList(1)
M = DoublyLinkedList(3)
N = DoublyLinkedList(5)
O = DoublyLinkedList(7)
Q = DoublyLinkedList(9)

DHead.next = M

M.prev = DHead
M.next = N

N.prev = M
N.next = O

O.prev = N
O.next = Q

Q.prev = O

find_number_withLL_instance = findNumberLL(array=head, number_to_find=number_to_find)
find_number_withDLL_instance = findNumberLL(array=DHead, number_to_find=number_to_find)

find_number_withDLL_instance.find_the_number()
find_number_withDLL_instance.find_the_number()