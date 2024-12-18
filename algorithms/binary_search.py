# binary search -> traditional binmary search and conditional based

# traditional search
class TraditionBinary:
    def __init__(self, array, number_to_find) -> None:
        self.array : list = array
        self.number_to_find = number_to_find

    def search(self):
        initial_index = 0
        final_index = len(self.array) - 1
        
        while initial_index >= final_index:
            central_index = initial_index + ((final_index - initial_index) // 2)

            sorted_array =self.array.sort()

            if sorted_array[central_index] == self.number_to_find:
                return central_index
            
            elif sorted_array[central_index] < self.number_to_find:
                initial_index = central_index + 1
            
            else:
                final_index = central_index - 1

        return False
    
# conditional search
class ConditionalBinary:
    def __init__(self, array, number_to_find) -> None:
        self.array : list = array
        self.number_to_find : int = number_to_find

    def search(self):
        initial_index = 0
        final_index = len(self.array) - 1

        while initial_index < final_index:
            central_index = (final_index + initial_index) // 2

            if self.array[central_index] == self.number_to_find:
                final_index = central_index
            else:
                initial_index = central_index + 1

        return initial_index

array = [1, 2, 3, 4, 5, 6, 7]
number_to_find = 3

tradBinSearch = TraditionBinary(array=array, number_to_find=number_to_find)
tradCondSearch = ConditionalBinary(array=array, number_to_find=number_to_find)

position = tradBinSearch.search()
print("From Traditional Binary Search: ", position)

position = tradCondSearch.search()
print("From conditional Binary Search: ", position)