"""Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200,'d':400}
Sample output: ({'a': 400, 'b': 400,'d': 400, 'c': 300})"""

#define two dictionaries
d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}

#Create an empty dictionary to hold the combined values
combined_dict = {}

#loop over the keys in d1 and thier values to combined dictionary
for key, value in d1.items():
    combined_dict[key] = value

#loop over the keys in d2 and their values to the combined dictionary
for key,value in d2.items():
    if(key in combined_dict):
        combined_dict[key]+=value
    else:
        combined_dict[key] = value

# print the combined dictionary
print(combined_dict)