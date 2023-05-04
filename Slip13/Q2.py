"""Q.2) Write a Python program to accept a string and from a given string where all occurrences of
its first character have been changed to '$', except the first char itself"""

def replace_first_char(string):
    if len(string) <= 1:
        return string
    first_char = string[0]
    return first_char + string[1:].replace(first_char, '$')

# Example usage:
string = 'banana'
new_string = replace_first_char(string)
print(new_string)  # b$nana