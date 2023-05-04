# Q.1) Write a Python program to get the 4
# th element from front and 4th element from last of a
# tuple. 

# In Python, a tuple is an ordered, immutable collection of elements. A tuple is similar to a list, but it cannot be modified once it is created. Tuples are defined using parentheses () and each element is separated by a comma. Here's an example of a tuple:

#create a tuple
my_tuple = (1,2,3,4,5,6,7,8,9)

#get the 4th element from front
fourth_front = my_tuple[3]

#get the 4th element from last
fourth_last = my_tuple[-4]

# print the results
print("4th element from front:", fourth_front)
print("4th element from last:", fourth_last)