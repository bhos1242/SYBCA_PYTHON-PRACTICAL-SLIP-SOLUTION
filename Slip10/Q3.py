"""Q.2) Write a Python program to count frequency of each character in a given string using user
defined function. """


def count_chars(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

string = input("Enter a string: ")
freq_dict = count_chars(string)
print("Frequency of each character in the string:")
for key, value in freq_dict.items():
    print(key, ":", value)
    