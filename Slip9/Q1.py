"""Q.1) Write a Python program to create a tuple using two different tuples. [10 M]
Q.2) Write a Python program to sort (ascending and descending) a dictionary by value. [20 M]
OR
Q.2) Write a Python program to count the occurrences of each word in a given sentenc"""

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
new_tuple = tuple1 + tuple2
print(new_tuple)



my_dict = {'apple': 10, 'banana': 5, 'orange': 20}

sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])

print(sorted_dict)


sentence = input("Enter a sentence: ")

# Split the sentence into a list of words
words = sentence.split()

# Create an empty dictionary
word_count = {}

# Loop through each word and increment its count in the dictionary
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the count of each word in the dictionary
for word, count in word_count.items():
    print(word, count)

