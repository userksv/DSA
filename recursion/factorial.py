def factorial(n: int):
    if n == 0: # base case
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))