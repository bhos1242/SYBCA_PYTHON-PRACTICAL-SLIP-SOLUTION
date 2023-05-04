# Q2) Write a Python program to print a dictionary where the keys are numbers between 1 and
# 15 (both included) and the values are square of keys.
# Sample Dictionary: {10: 100, 20: 400, 30: 900, 40: 1600, 50: 2500}

#create empty dictionary
squares_dict = {}

#loop over number from 1 to 15(both included)
for num in range(1,16):
    squares_dict[num] = num**2

#print the dictionary
print(squares_dict)
