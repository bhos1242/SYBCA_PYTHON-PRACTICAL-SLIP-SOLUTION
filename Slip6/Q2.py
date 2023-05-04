"""Q.2) Write a Python program to create and display all combinations of letters, selecting each
letter from a different key in a dictionary. [20 M]
Sample data: {'1':['a','b'], 2':['c','d']}
Expected Output:
ac
ad
bc
bd
"""

data = {'1': ['a', 'b'], '2': ['c', 'd']}

for letter1 in data['1']:
    for letter2 in data['2']:
        print(letter1 + letter2)
