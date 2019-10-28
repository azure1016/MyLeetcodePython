class Solution:
    def decodeString(self, s):
        res = ""
        count = 0
        stack = []
        for ch in s:
            if ch.isnumeric():
                count = count * 10 + int(ch)
            elif ch == '[':
                stack.append(count)
                stack.append('[')
                count = 0
            elif ch == ']':
                repeat = ""
                while stack[-1] != '[':
                    repeat += stack.pop()
                stack.pop()  # pop out "["
                count = stack.pop()
                stack.append(count * repeat[::-1])
                count = 0
            else:
                stack.append(ch)
        return "".join(stack)
    def test(self, encoding, expected_decoding):
        result = self.decodeString(encoding)
        print(result == expected_decoding)

encoding = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
sol = Solution()
decoding_expected = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
sol.test(encoding, decoding_expected)
