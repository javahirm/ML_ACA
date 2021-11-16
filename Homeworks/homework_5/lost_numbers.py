def absent_numbers(arr):
    return set(range(1, len(arr) + 1)) - set(arr)


nums = [4, 2, 4, 7, 5, 4, 7]
print(absent_numbers(nums))
