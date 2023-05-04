# Q.2) Write a Python program to accept n elements in a set and find the length of a set, maximum,
# minimum value and the sum of values in a set. (Don’t use built-in function)

n = int(input("Enter the number of elements in the set: "))
my_set = set()

for i in range(n):
    elem = int(input("Enter element {}:" .format(i+1)))
    my_set.add(elem)

#Finding the length of the set
length = 0
for elem in my_set:
    length += 1
print("Length of set is:",length)

#Finding the maximun value in the set
max_val = None
for elem in my_set:
    if max_val is None or elem > max_val:
        max_val = elem
print("Maximum value in the set is:", max_val)

#Finding the minimum value in the set
min_val = None
for elem in my_set:
    if min_val is None or elem <min_val:
        min_val = elem
print("Minimum value in the set is:",min_val)

#Finding the sum of vlaue in set
sum = 0
for elem in my_set:
    sum = sum+elem;
print("Sum of values in the set is:",sum)