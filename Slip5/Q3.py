# Q.2) Write a Python program to create a dictionary from two lists without losing duplicate
# values.
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII':
# {3}, 'Class-V': {1}})


from collections import defaultdict

keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]

result = defaultdict(set)

for k, v in zip(keys, values):
    result[k].add(v)

print(dict(result))
