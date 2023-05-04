# Q.2) Write a Python program to find set difference, union, intersection and symmetric
# difference.



set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#set difference
diff_set = set1.difference(set2)
print("Set difference:", diff_set)

#union
union_set = set1.union(set2)
print("Union Set:",union_set)

#intersection
intersection_set = set1.intersection(set2)
print("Intersection set:",intersection_set)

#symmetric diffrence
symm_diff_set = set1.symmetric_difference(set2)
print("Symmetric difference set:",symm_diff_set)
