#judge if a string could be permuted to another string
class Solution:
    def permuteTo(self, str1, str2):         
        dc1 = self.toDict(str1)
        dc2 = self.toDict(str2)
        return dc1 == dc2

    def toDict(self, str):
    	dc = {}
    	for a in str:
    		if a not in dc:
    			dc[a] = 1
    		else:
    			dc[a] = dc[a] + 1
    	return dc

#test
test = Solution()
print(test.permuteTo("tes m ", "tes m"))
print(test.permuteTo("low", "owl"))
print(test.permuteTo("!*sd", " !*sd"))

#output
#False
#True
#False