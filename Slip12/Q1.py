"""Q.1) Write a Python program to find the length of a string without using built-in function"""

def string_length(s):
    count = 0
    for i in s:
        count += 1
    return count

# example usage
string = "Hello, World!"
print("Length of string:", string_length(string))