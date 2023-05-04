"""Q.1) Write a Python program to sort the tuple T=(4,2,6.8,1.8,10) ."""

"""In the Python programming language, tuples are immutable objects, which means that once created, we cannot modify their contents. Therefore, we cannot sort the elements of a tuple directly."""

# define the tuple T
T = (4, 2, 6.8, 1.8, 10)

# convert the tuple to a list, sort the list, and convert it back to a tuple
sorted_T = tuple(sorted(list(T)))

# print the sorted tuple
print(sorted_T)
