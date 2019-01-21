#reverse a string
class Solution:
    #only works for ascii, not for utf8
    def reverse(self, str):         
        return str[::-1]

#test
test = Solution()
a = "anything"
#b = a.decode('utf8')
#string has no attribute decode
#print(test.reverse("anything".decode('utf8')))
#print(test.reverse(b))
print(test.reverse("tes m "))
print(test.reverse("low"))
print(test.reverse("!*sd"))

#output
#False
#False
#True
#True