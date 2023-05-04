"""Q.1) Write a Python program to create a tuple of n numbers and print maximum, minimum, and
sum of elements in a tuple. """

n = int(input("Enter a number: "))

t = tuple(map(int,input("Enter the elemets seperated by space: ").split()))

print("Max of tuple",max(t))
print("Min of tuple",min(t))
print("Sum of tuple",sum(t))