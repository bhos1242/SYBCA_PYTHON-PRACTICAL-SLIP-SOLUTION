"""Q.2) Write a Python program to accept n numbers in list. Find average of list and sort it in
descending order"""

n = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(n):
    num = float(input("Enter a number: "))
    lst.append(num)

avg = sum(lst)/n

print("Average of the list is:", avg)

lst.sort(reverse=True)

print("List sorted in descending order:", lst)
