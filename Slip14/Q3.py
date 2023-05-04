"""Q.2) Write a Python program to define class to find validity of a string of parentheses, '(', ')', '{',
'}', '[' and ']. These brackets must be in the correct order, for example "()" and "()[]{}" are valid
but "[)", "({[)]" and "{{{" are invalid."""

class ParenthesesValidator:
    def __init__(self, string):
        self.string = string
    
    def is_valid(self):
        stack = []
        for char in self.string:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or not self.matches(stack.pop(), char):
                    return False
        return not stack
    
    def matches(self, left, right):
        return (left == '(' and right == ')') or (left == '[' and right == ']') or (left == '{' and right == '}')

# Example usage:
validator = ParenthesesValidator('()[]{}')
print(validator.is_valid())  # True

validator = ParenthesesValidator('()[{}]')
print(validator.is_valid())  # True

validator = ParenthesesValidator('({[)]')
print(validator.is_valid())  # False

validator = ParenthesesValidator('{{{')
print(validator.is_valid())  # False
