"""Q.2) Write a Python program which finds sum of digits of a number.
Example n=130 then output is 4 (1+3+0)"""

n = int(input("Enter a number: "))
sum_of_digits = 0

while n > 0:
    remainder = n % 10
    sum_of_digits += remainder
    n = n // 10

print("Sum of digits:", sum_of_digits)
