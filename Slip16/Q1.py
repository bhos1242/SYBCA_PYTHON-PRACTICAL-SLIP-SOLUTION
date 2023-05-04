"""User
Q.1) Write a Python program to create tuple of n numbers, print the first half values of tuple in
one line and the last half values of tuple on next line"""

n = int(input("Enter the number of values: "))

t = tuple(range(1,n+1))

midpoint = len(t)//2
# (//). This gives the index of the first element in the second half of the tuple.
print("First half:",end=" ")
for i in range(midpoint):
    print(t[i], end=" ")

print("\nLast half:",end = " ")
for i in range(midpoint,len(t)):
    print(t[i],end = " ")