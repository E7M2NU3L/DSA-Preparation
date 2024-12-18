# arrays -> static and dynamic arrays

number_to_find = -1
array_of_number = [1, 2, 3, 4, 5, 6]


pos = 0
while True:
    if pos >= len(array_of_number):
        print("The number {0} is not found in the list".format(number_to_find))
        break

    if array_of_number[pos] == number_to_find:
        print("The number {0} is in the position {1}".format(pos, array_of_number[pos]))
        break

    pos = pos + 1