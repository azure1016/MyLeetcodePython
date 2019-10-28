import functools
class RomanNumber:
    def roman_to_integer(self, s):
        T = {'I':1, "V": 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        return functools.reduce(lambda cur_sum, i: cur_sum + (-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]), reversed(range(len(s)-1)), T[s[-1]])
    # this solution  might be wrong. dependent on the requirement of problem. here, 'DXXVIIII' is invalid. (but idk why)
    def validate(self, s):
        T = {'I':1, "V": 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        exception = 0
        for i in reversed(range(len(s) - 1)):
            if T[s[i]] < T[s[i+1]]:
                exception += 1
                if exception > 1: return False
            else: exception = 0
        return exception <= 1
    
    def test_two(self, s):
        print(self.roman_to_integer(s))
        print(self.validate(s))

RomanNumber().test_two("DXXVIIII")
    

