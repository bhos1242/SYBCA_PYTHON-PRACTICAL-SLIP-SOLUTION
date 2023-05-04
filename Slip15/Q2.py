"""Q.2) Write a Sequential search function which searches an item in a sorted list. The function
should return the index of element to be searched in the list. """

def sequential_search(sorted_list, item):
    """
    Performs a sequential search on a sorted list to find the index of an item.

    Parameters:
    sorted_list (list): A list of sorted items.
    item (int): The item to search for.

    Returns:
    int: The index of the item in the list, or -1 if the item is not found.
    """
    # Set the initial index to 0
    index = 0

    # Loop through the list until the end is reached or the item is found
    while index < len(sorted_list) and sorted_list[index] < item:
        index += 1

    # Check if the item was found
    if index < len(sorted_list) and sorted_list[index] == item:
        return index
    else:
        return -1

# Define a sorted list
my_list = [2, 4, 6, 8, 10, 12]

# Call the sequential_search function to search for an item
result = sequential_search(my_list, 8)

# Print the result
if result != -1:
    print(f"Item found at index {result}.")
else:
    print("Item not found.")

