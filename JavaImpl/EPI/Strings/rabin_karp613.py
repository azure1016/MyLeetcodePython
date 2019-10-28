import functools

def rabin_karp(t, s):
    # s is not a substring of t
    if len(s) > len(t): return -1

    BASE = 29 # I think BASE to be a primary number would be better? or not?
    # hash codes for the substring of t and s
    t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)
    power_s = BASE ** max(len(s) - 1, 0) # BASE * |s-1|

    for i in range(len(s), len(t)):
        # checks the two substrings are actually equal or not, to protect
        # against hash collision
        if t_hash == s_hash and t[i-len(s):i] == s:
            return i - len(s) # found a match
        # uses rolling ahsh to compute the hash code
        t_hash -= ord(t[i-len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])

    # try to match s and t[-len(s):], don't forget this! because this is not
    # included in the for loop
    if t_hash == s_hash and s == t[-len(s):]:
        return len(t) - len(s)
    return -1 # s is not a substring of t


def test(t, s):
    result = rabin_karp(t, s)
    if result == -1: print("no match")
    else:
        print("find match at {}, s: {}, t: {}".format(result, s, t[result:result + len(s)]))

t = "appleisanpinappleright"
s = "sanp"
test(t, s)

