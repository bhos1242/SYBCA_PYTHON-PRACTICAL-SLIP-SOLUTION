# Write a Python program to print the set difference and a symmetric difference of two sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Set difference
diff1 = set1 - set2
diff2 = set2 - set1

print("Set difference of set1 and set2:", diff1)
print("Set difference of set2 and set1:", diff2)

# Symmetric difference
sym_diff = set1 ^ set2

print("Symmetric difference of set1 and set2:", sym_diff)
