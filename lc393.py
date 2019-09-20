class Solution:
    #TLE
    def validUtf8(self, data):
        i, lentgh = 0, 0
        while i < len(data):
            bin_str = bin(data[i])
            if not bin_str[0]:
                i += 1
                continue
            elif bin_str.startswith('110'): # 2 bytes
                if i+1 >= len(data): return False
                elif not bin(data[i+1]).startswith("10"):return False
                else:
                    i += 2
                    continue
            elif bin_str.startswith('1110'):
                if i+2 >= len(data):return False
                elif not (bin(data[i+1]).startswith('10') and bin(data[i+2]).startswith('10')): return False
                else:
                    i+= 3
                    continue
            elif bin_str.startswith('11110'):
                if i+3 >= len(data): return False
                elif not (bin(data[i+1]).startswith('10') and bin(data[i+2]).startswith('10') and bin(data[i+3]).startswith('10')): return False
                else:
                    i+= 4
                    continue
            else: return False
        return True