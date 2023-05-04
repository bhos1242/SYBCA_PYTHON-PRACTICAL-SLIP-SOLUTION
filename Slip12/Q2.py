"""Q.2) Write a Python program to accept string and remove the characters which have odd index
values of a given string using user defined function"""

def remove_odd_index_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i%2 == 0:
            new_string += string[i]
    return new_string

string = input("Enter a string: ")
new_string = remove_odd_index_chars(string)
print("Original string:", string)
print("New string after removing odd-index characters:", new_string)
