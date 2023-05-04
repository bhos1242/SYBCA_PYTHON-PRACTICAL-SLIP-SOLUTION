"""Q.1) Write a program which prints Fibonacci series of a number."""

n = int(input("Enter the number: "))

a = 0
b=1

print(a,b, end =" ")

for i in range(2,n):
    c = a + b
    print(c,end=" ")

    a = b
    b = c