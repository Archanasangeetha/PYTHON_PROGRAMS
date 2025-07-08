# Remove duplicates from a sorted array

def remove_duplicates_sorted(arr):
    """
    Removes duplicates from a sorted array in-place and returns a new list of unique elements.
    """
    if not arr:
        return []
    index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]
    return arr[:index + 1]

# Take input from the user
user_input = input("Enter sorted numbers separated by spaces: ")
arr = [int(x) for x in user_input.split()]
print(remove_duplicates_sorted(arr))
