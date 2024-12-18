# it is a priority queve
# here it consists of min heap where it is a binary with a minimum number is on the top
# if we pop of an element from the tree the tree is seperated and then the tree decides the sucessor of the root node based on the minimum conditions.
# heap push -> pushing new item where it checks the position it should fit in the binary tree, swapping begins with checking if the number added on the end is bigger from it's parent node
# heap peek -> it is the minimal value
# heap sort, it is repeatedly pop of the minimum -> O(nlogn) time complexity which is extremely good and space cmplexity of O(1)

import heapq

# min heap
A = [-4, 3, 1, 0, 6, 8, 4, 7, 17]
heapq.heapify(A)
print(A)

# heap push O(logn)
heapq.heappush(A, 12)
print("After heap push")
print(A)

# heap pop -> O(log2n)
minimum_val = heapq.heappop(A)
print(minimum_val)

# heap sort
def heapsort(array):
    heapq.heapify(array)
    n = len(array)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(array)
        new_list[i] = minn

    return new_list
test = [3, 2, 5, 4, 6, 7,11, 42, 12, 134, 65, 34, 52]
print(heapsort(test))

# heap push pop
heapq.heappushpop(A, 99)
print(A) 

# max heaps
# largest value
test2 = [2, 5, 4, 1, 6, -1, -4, -2, 6, 456, 6, 23, 99, 87, 56, -98]
for i in range(len(test2)):
    test2[i] = -test2[i]

heapq.heapify(test2)

print(test2)

largest_val = -heapq.heappop(test2) 
print(largest_val)