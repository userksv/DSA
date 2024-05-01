
def fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n-1)"""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci(n - 1)
        return(a + b, a)
    
def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)
    
print(fibonacci(20))
print(bad_fibonacci(20))

import math
math.pow()      