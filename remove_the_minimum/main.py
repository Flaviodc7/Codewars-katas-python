def remove_smallest(numbers):
    if len(numbers):
        minimum = min(numbers)
        result = list(numbers)
        result.remove(minimum)
        return result
    else:
        return []


print(remove_smallest([1, 2, 3, 4, 5]))
