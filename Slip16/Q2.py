"""Q.2) Write a Python program which prints fibonacci series of a number"""



n = int(input("Enter the nubmer : "))

a = 0
b = 1

print(a, b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")

    a = b
    b = c



