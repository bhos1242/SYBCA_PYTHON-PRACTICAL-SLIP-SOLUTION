"""Q.1) Write a Python program to accept the strings which contains all vowels"""

def contains_all_vowels(string):
    vowels = set('aeiou')
    return vowels.issubset(string.lower())

# Driver code
string = input("Enter a string: ")
if contains_all_vowels(string):
    print("The string contains all vowels")
else:
    print("The string does not contain all vowels")
