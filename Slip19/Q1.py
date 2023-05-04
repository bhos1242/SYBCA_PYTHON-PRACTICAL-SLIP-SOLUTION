# Q.1) Write a Python program to calculate the average of numbers in a given list

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

numbers = [1,2,3,4,5,6,7]

average = calculate_average(numbers)
print("The average is:",average)