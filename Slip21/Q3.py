"""Q.2) Write a Sequential search function which searches an item in a sorted list. The function
should return the index of element to be searched in the list."""

def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        elif arr[i] > x:
            return -1

    return -1

# Driver code
lst = [2, 5, 7, 10, 14, 18, 21]
x = 14
index = sequential_search(lst, x)

if index == -1:
    print(f"{x} not found in the list")
else:
    print(f"{x} found at index {index}")