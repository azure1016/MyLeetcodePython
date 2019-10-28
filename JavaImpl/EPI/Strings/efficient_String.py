'''
String is immutable, so:
1. adding elements to the front of string n times, time complexity: O(n^2)
2. adding elements to the end of string n times, time complexity?
3. replacing elements by index in string n times, time complexity?
4. Note that some implementation ...
5. example: converting integers to strings

 How to implement a string class that supports efficient operation as 'adding elements to the end of string' and 
'replacing elements by index in string' ? 


'''
import functools
import string
def string_to_int(s):
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

# this the wrong implementation: ord() returns the ascii code!
def string_to_int_2(s):
    start = 1 if s[0] == '-' else 0
    return functools.reduce(lambda running_sum, c: running_sum * 10 + ord(c), s[start:], 0) * (1 if start == 0 else -1)

def test(s):
    print(string_to_int(s))
    print(string_to_int_2(s))

test("-314")