# the functions which repeats on it self
# it contains a call stack
# it has O(2^n) time complexity
# space complexity -> O(n)

def fibonacci(n):
    # base case -> 1
    if n == 0:
        return 0
    
    # base case -> 2
    elif n == 1:
        return 1
    
    # recursive functionality
    else:
        return n + fibonacci(n-1)
    
response = fibonacci(9)
print(response)