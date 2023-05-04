# Q.2) Write a Python program to accept n numbers in list and remove duplicates from a list.

n = int(input("Enter the size of list: "))
num_list = []
for i in range(n):
    num = int(input("Enter a number: "))
    num_list.append(num)

# Using set()
unique_list = list(set(num_list))
print("Unique list using set(): ", unique_list)

# Using for loop and empty list
new_list = []
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print("Unique list using for loop: ", new_list)
