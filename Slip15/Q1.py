""") Write a python program to check if a string is a Palindrome or not."""

string = input("Enter a string: ")

string = string.lower().replace(" ","")

if string == string[::-1]:
    print("The string is a pallindrome.")
else:
    print("The string is not pallindrome")