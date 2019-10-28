"""
2 <= b1, b2 <= 16
"""
# total time complexity for this 
def convert_base(num_as_stirng, b1, b2):
    def construct_from_base(num_as_int, base):
        # note that this function has O(m^2) time complexity, m = log_base^num_as_int
        return ("" if nums_as_int == 0 else construct_from_base(num_as_int // base, base) +
        string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(lambda x, c: x * b1 + string.hexdigits.index(c.lower()), num_as_string[is_false:], 0)
    return ('-' if is_negative else "") + ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))