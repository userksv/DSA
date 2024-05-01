class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack():
    """Simple implementation of a Stack Data Structure"""
    def __init__(self) -> None:
        self.data = []
    
    def __str__(self) -> str:
        return f'{self.data}'
    
    def __len__(self):
        return len(self.data)
    
    def push(self, value: any):
        self.data.append(value)
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data.pop()
    
    def is_empty(self):
        return len(self.data) == 0

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]
    

S = ArrayStack()
# print(S.top())
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
print(S)