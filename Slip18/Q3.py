"""Q.2) Write a Python program to count frequency of each character in a given string using user
defined function."""

def count_chars(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char]+=1
        else:
            freq[char] = 1
    return freq

my_string = input("Enter a string: ")
char_freq = count_chars(my_string)

for char, freq in char_freq.items():
    print("Character '{}' appears {} time(s) in the string.".format(char,freq))