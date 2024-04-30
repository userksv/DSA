def binary_search(data: list, target: int, low: int, high: int):
    # The binary search algorithm runs in O(log n) time for a sorted sequence with n elements.
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
        
data = [i for i in range(1_000_000)]

print(binary_search(data, 324, 0, len(data)))
