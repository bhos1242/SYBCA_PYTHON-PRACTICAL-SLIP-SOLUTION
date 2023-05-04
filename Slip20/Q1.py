# Q.1) Write an anonymous function to calculate area of square. 

area_of_square = lambda side:side**2
"""Lambda functions are a way to create small, one-time use functions in Python. They are called "anonymous" because they have no name and are not defined with the def keyword like regular functions. Instead, lambda functions are defined using the lambda keyword followed by the arguments, a colon, and the expression that will be executed when the function is called."""
# Example usage
area = area_of_square(4)
print("Area of square:", area)