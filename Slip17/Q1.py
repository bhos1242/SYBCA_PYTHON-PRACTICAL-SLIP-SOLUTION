# Q.1) Write a Python program to accept and convert string in uppercase or vice versa.

#Accept a string input from the user
string = input("Enter a string: ")

choice = input("Do you want to convert the string to uppercase or lowercase?(U/L): ")

if choice == 'U':
    string = string.upper()
elif choice == 'L':
    string = string.lower()
else:
    print("Invalid Choice!")

print("Converted string:", string)
