"""Q.2) Write a Python program to create a set with any 3 weekdays. Add single element to the set
and print it. Add multiple elements and print the set. """

# create a set with any 3 weekdays
weekdays = {"Monday", "Wednesday", "Friday"}

# add a single element to the set
weekdays.add("Tuesday")
print("After adding 'Tuesday':", weekdays)

# add multiple elements to the set
weekdays.update(["Thursday", "Saturday", "Sunday"])
print("After adding 'Thursday', 'Saturday', and 'Sunday':", weekdays)
