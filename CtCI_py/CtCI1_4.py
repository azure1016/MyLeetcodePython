class Solution:
    def replace(self, str, before, after):
        new_str = []
        for a in str:
            if a ==  before:
                a = after
            new_str.append(a)
        return new_str


s = Solution()
str = s.replace("Mr John Smith", ' ', "%20")
print(str)