from timer import timer

array = [i for i in range(1_000_000)]

@timer
def binary_search(array:list, target: int):
    high_index = len(array) - 1
    low_index = 0
    while low_index <= high_index:
        mid = (high_index + low_index) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            low_index = mid + 1
        else:
            high_index = mid - 1
    return -1

@timer
def linear_search(array: list, target: int):
    i = 0
    while i < len(array):
        if target == array[i]:
            return i
        i += 1
    return -1

print(binary_search(array, -1))
print(linear_search(array, -1))