"""Q.2) Write a Python program to check if a given key already exists in a dictionary. If key exists
replace with another key/value pair."""

#Define a dictionary
my_dict ={"apple":2,"banana":3,"orange":5}

key = input("Enter a key: ")

if key in my_dict:
    new_key = input("Enter a new key:")
    new_value = input("Enter a new value: ")

    my_dict[new_key] = new_value
    del my_dict[key]

print(my_dict)