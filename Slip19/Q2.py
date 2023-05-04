"""Q.2) Write a Python function to get a string made of the first 2 and the last 2 chars from a given
string. If the string length is less than 2, it return empty string.
Sample String: 'General12' Expected Result: 'Ge12'
Sample String: 'Ka' Expected Result: 'KaKa'
Sample String: ' K' Expected Result: Empty String """

def get_string(s):
    if len(s)<2:
        return ''
    else:
        return s[:2]+s[-2:]
    
print(get_string('General12'))
print(get_string('Ka'))
print(get_string('K'))