# Q.1) Write a Python function to check whether a number is in a given range.

def check_range(num, start, end):
    if num in range(start, end+1):
        print(f"{num} is within the range of {start} and {end}.")
    else:
        print(f"{num} is not within the range of {start} and {end}.")

check_range(17,1,10)