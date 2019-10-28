def get_valid_part(s):
    def is_valid_part(s):
        #'00', '000', '01', etc. are not valid, but '0' is valid
        return len(s) == 1 or (s[0] != 0 and int(s) <= 255)
    
    result, parts = [], [None] * 4
    for i in range(1, min(4, len(s))):# s.length may < 4???
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)): # part1 is at least 1 bit long
                parts[1] = s[i:j+i]
                if is_valid_part(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2] = s[j+i:j+i+k]
                        parts[3] = s[i+j+k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append(".".join(parts))
    return result

def get_vaild_part_recr(s, periods):
    # the address is filled with 'periods' of periods; so dividen into periods+1 parts
    def is_valid_part(s, d): # d is the maximum number of digits of a part
        return len(s) == 1 or (s[0] != 0 and int(s) <= 2 ** (d) - 1)
    
    def recursive_helper(s, periods, parts):
        if periods == 0:
            if is_valid_part(s, 8): 
                parts[-1] = s
                result.append(".".join(parts))
            else: return
        for i in range(1, min(4, len(s))):
            new_parts = list(parts)
            if is_valid_part(s[:i], 8):
                new_parts[3-periods] = s[:i]
                recursive_helper(s[i:], periods - 1, new_parts)

    result = []
    recursive_helper(s, periods, [None] * 4)
    return result



def test(ip):
    ips = get_valid_part(ip)
    print(len(ips) == 9)
    ips_recr = get_vaild_part_recr(ip, 3)
    print(ips_recr)
    print(len(ips_recr) == 9)
    
    
test("19216811")


