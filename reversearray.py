# Reverse an array using slicing
def reverse_array(arr):
    return arr[::-1]

print(reverse_array(['a', 'b', 'c', 'd', 'e', 'f', 'g']))  # Output: ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# Reverse an array manually (without slicing)
def reverse_array_manual(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_array_manual([3, 1, 4, 1, 5, 9]))  # Output: [9, 5, 1, 4, 1, 3]
