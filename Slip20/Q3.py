"""Q.2) Write a Python program to remove special symbols/Punctuation from a given string."""

import string


def remove_punctuation(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

#Example usage:
text = "Hello, World!"
clean_text = remove_punctuation(text)
print(clean_text)