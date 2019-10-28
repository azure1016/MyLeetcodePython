'''
page 74
use nested loops is not reccommend because of its repetitiveness in code and its inflexibility
use recursion instead!
'''

# the mapping from digit to corresponding characters
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonics(phone_number):
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            # all digits are processed, so add partial_mnemonics to mnemonics
            # (We add a copy since subsequent calls modify partial_mnemonic.)
            mnemonics.append("".join(partial_mnemonic))
        else:
            # Try all possible characters for this digit
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)
    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics

def test(phone_number):
    for row in phone_mnemonics(phone_number):
        print(row)

test("226")