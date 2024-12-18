# time and space complexity

# N*N is like merging elements in an array as a couple ex : [1, 2, 3, 4, 5] 
# here clubbing (1, 2), (1, 3).... (5, 5) is like creating a static N and moviing N moving withvit it is like 5 * 5 times.
# it is a O(n^2) problem

# the functions can be linear O(n) which is fast and quadratic functions O(n*n) , O(n^3) etc., which is a bit slower

import time
array_of_numbera = [1, 2, 3, 4, 5]

list_clubbed = []
time_before = time.gmtime()
for i in array_of_numbera:
    for j in array_of_numbera:
        list_clubbed.append((i, j))
time_after = time.gmtime()

print("Before : {0}, After: {1}".format(time_before, time_after))
print(list_clubbed)

# apce complexity => is the amount of space it holds to store th numbers
# O(n) is the problem when an array is squared and returned the exact amount of N integers

list_squared = []
for i in array_of_numbera:
    list_squared.append(i**2)

print(list_squared)

# there can be sequence of conditions to big O notation -> O(n^2 + 2n + 1)
# that must be reduced to o(n^2) bacause it is the biggest curve maker in this problem

