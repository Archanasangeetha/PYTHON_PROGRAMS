# Reverse an array using slicing

def reverse_array(arr):
    """
    Returns a new list that is the reverse of the input list.
    """
    return arr[::-1]  # Slice in reverse order

# Test cases
print(reverse_array([3, 1, 4, 1, 5, 9]))  # Output: [9, 5, 1, 4, 1, 3]
print(reverse_array([1, 2, 3, 4, 5]))     # Output: [5, 4, 3, 2, 1]
print(reverse_array([1, 2, 3]))           # Output: [3, 2, 1]
