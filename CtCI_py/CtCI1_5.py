class Solution:
    def zip_it (self, str):
        new_str = []
        count = 0
        prev = str[0]
        for a in str:
        	if a == prev:
        		count = count + 1
        		continue
        	else:
        		new_str.append(prev)
        		new_str.append(count)
        		prev = a
        		#new_str.append(a)
        		count = 1
        new_str.append(prev)
        new_str.append(count)
        return new_str

s = Solution()
#str = s.zip_it("  aaabbbddccccf")
#print(str)
str2 = s.zip_it("  aaabbbddccccfff")
print(str2)
