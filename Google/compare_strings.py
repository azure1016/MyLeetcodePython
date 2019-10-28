# compare strings
from bisect import *
class Comparator:
    def string_to_frequency(self, s):
        base = s[0]
        freq = 0
        for ch in s:
            if ch < base:
                base = ch
                freq = 1
            elif ch == base:
                freq += 1
        return freq

    def compare(self, As, Bs):
        A = As.split(', ')
        B = Bs.split(', ')
        freq_a = sorted([self.string_to_frequency(s) for s in A])
        freq_b = [self.string_to_frequency(s) for s in B]
        result = []
        for b in freq_b:
            ind = bisect_left(freq_a, b) # strictly smaller than freq_b
            result.append(ind)
        return result

string1 = 'abcd, aabc, bd'
string2 = 'aaa, aa'
sol = Comparator()
res = sol.compare(string1, string2)
print(res)