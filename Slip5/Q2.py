"""Q.2) Write a function to calculate the sum of numbers from 0 to n. """


def sum_n(n):
      sum = 0
      for num in range(0,n+1):
        sum = sum+num

      return sum

print("Sum:",sum_n(5))