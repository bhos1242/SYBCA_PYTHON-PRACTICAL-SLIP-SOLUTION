"""Q.1) Write a Python program to print average of all elements of sets. [10 M]
Q.2) Write a Python program to match key values in two dictionaries. [20 M]
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y
OR
Q.2) Write a Python function to multiply all the numbers in a list. [20 M]
Sample-List: (8, 2, 3, -1, 7)
Expected Output: -336"""

# Define a set of numbers
my_set = {1, 2, 3, 4, 5}

# Find the sum of all elements in the set
sum_of_elements = sum(my_set)

# Find the total number of elements in the set
total_elements = len(my_set)

# Calculate the average of all elements
average = sum_of_elements / total_elements

# Print the average
print("Average of all elements in the set:", average)



dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

# Iterate through the keys in dict1 and check if they are also in dict2
for key in dict1.keys():
    if key in dict2.keys():
        # If the value associated with the key is also the same, print a message
        if dict1[key] == dict2[key]:
            print(f"{key}: {dict1[key]} is present in both dict1 and dict2")


def multiply_list_numbers(numbers):
    """
    Multiplies all the numbers in a list and returns the result
    """
    result = 1
    for num in numbers:
        result *= num
    return result
