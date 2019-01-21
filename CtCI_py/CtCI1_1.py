#judge if all the character in a string is distinct
class Solution:
    #solution 1
    def allDistinctLetter1(self, str):
        if len(str) > 256:
            return False
        barrel = {}
        for a in str:
            if a in barrel:
                return False
            else:
                #val = barrel.get(a) + 1
                barrel[a] = 1

        return True

#test
test = Solution()
print(test.allDistinctLetter1("anything"))
print(test.allDistinctLetter1("tes m "))
print(test.allDistinctLetter1("low"))
print(test.allDistinctLetter1("!*sd"))

#output
#False
#False
#True
#True