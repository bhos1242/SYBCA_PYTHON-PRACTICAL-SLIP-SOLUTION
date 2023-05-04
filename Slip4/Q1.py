"""Write a Python program to find the repeated items of a tuple"""

#define a tuple
my_tuple = (1,2,3,2,4,5,4,6,7,6)

#find the repeated items
repeated_items = set()
unique_items = set()

for item in my_tuple:
    if item in unique_items:
        repeated_items.add(item)
    else:
        unique_items.add(item)

# print the repeated items
print("Repeated items in the tuple:", repeated_items)