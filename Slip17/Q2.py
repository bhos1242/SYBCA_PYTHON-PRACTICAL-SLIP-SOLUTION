# Q.2) Write a Python program which accepts an integer value ‘n’ and display all prime
# numbers till ‘n’.

n = int(input("Enter the number:"))

#Check if a number is prime or not
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num*0.5)+1):
        if num%i ==0:
            return False
    return True

# Loop through all numbers up to n and check if they are prime
print("Prime numbers up to", n, ":")
for i in range(2, n+1):
    if is_prime(i):
        print(i)