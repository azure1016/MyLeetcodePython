'''
page 75

The precise time complexity is a function of the lengths of the terms, which is 
extremely hard to analyze.

Each successive number can have at most twice as many digits as the previous number
-- This happens when all digits are different. This means the maximum length number has
length no more than 2^n. Since there are n iterations and the work in each iteration is
proportional to the length of the number computed in the iteration, a simple bound on
the time complexity is O(n*2^n)

'''

def look_and_say(n):
    def next_number(s): # use string as the parameter because you'll use string to store the 
        # intermediate result
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i+1]:
                count += 1
                i += 1
            # result += str(count) + s[i] # don't use string to store result coz its expensive to modify
            result.append(str(count) + s[i])
            i += 1
        return "".join(result)

    s = '1' # the game starts with '1'
    for _ in range(1, n):
        s = next_number(s)
    return s

# pythonic implementation of look_and_say()
def look_and_say_pythonic(n):
    s = '1'
    for _ in range(n-1):
        s = "".join(str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s

def test(n):
    print(look_and_say(n))
    print(look_and_say(n))

test(1)
test(7)