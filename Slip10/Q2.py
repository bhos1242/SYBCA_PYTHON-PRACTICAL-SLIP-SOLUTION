"""Q.2) Write a Python program to create a dictionary from a string.
Sample String: ’Hello all’
Expected output: {'e': 1, 'o': 1, 'a': 1, 'l': 4, 'H': 1}"""

str = str(input("Enter a string: "))

dict = {}

for char in str:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print(dict)