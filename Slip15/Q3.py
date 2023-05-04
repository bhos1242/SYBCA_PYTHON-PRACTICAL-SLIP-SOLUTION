"""Q.2) Write a Python program which finds sum of digits of a number. [20 M]
Example n=135 then output is 9 (1+3+5)"""

n = int(input("Enter a number: "))

str_n = str(n)

sum = 0
for char in str_n:
    char = int(char)
    sum = sum+char

print("Sum: ",sum)
