"""Q.2) Write a Python program to perform given operations on set. [20 M]
a. check whether 2 sets are equal or not
b. Symmetric difference
c. Intersection of sets
d. Find maximum and the minimum value in a set."""

# define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# a. check whether two sets are equal or not
if set1 == set2:
    print("The two sets are equal")
else:
    print("The two sets are not equal")

# b. symmetric difference
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric difference of the two sets:", symmetric_difference)

# c. intersection of sets
intersection = set1.intersection(set2)
print("Intersection of the two sets:", intersection)

# d. maximum and minimum value in a set
max_value = max(set1)
min_value = min(set2)
print("Maximum value in set1:", max_value)
print("Minimum value in set2:", min_value)
