"""Q.2) Write a Python program which accepts 6 integer values and prints “DUPLICATES” if any
of the values entered are duplicates otherwise it prints “ALL UNIQUE”.
Example: Let 5 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be printed"""

# get 6 integers from the user
nums = []
for i in range(6):
    num = int(input(f"Enter integer {i+1}: "))
    nums.append(num)

# check for duplicates
if len(set(nums)) == len(nums):
    print("ALL UNIQUE")
else:
    print("DUPLICATES")