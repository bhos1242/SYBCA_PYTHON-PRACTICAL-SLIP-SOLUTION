"""Q.2) Write a Python program which accept an integer value ‘n’ and display all prime numbers
till ‘n’."""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

print(f"Prime numbers up to {n}: ")
for i in range(2, n+1):
    if is_prime(i):
        print(i, end=" ")
