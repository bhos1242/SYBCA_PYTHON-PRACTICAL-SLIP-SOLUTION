"""Q.2) Write a Python program to reverse a given number"""

n = int(input("Enter the number: "))

str_n = str(n)

print(str_n[::-1]);

"""num = int(input("Enter a number: "))
rev_num = 0

while num > 0:
    remainder = num % 10
    rev_num = (rev_num * 10) + remainder
    num = num // 10

print("The reverse of the number is:", rev_num)"""