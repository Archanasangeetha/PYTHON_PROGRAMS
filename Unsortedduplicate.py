# Remove duplicates from an unsorted array while preserving order

def remove_duplicates_unsorted(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Take input from the user
user_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in user_input.split()]
print(remove_duplicates_unsorted(arr))
