import math
class Solution(object):
    # def reverse(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     sign = 1 if x > 0 else -1
    #     s = abs(x)
    #     num_digits = math.floor(math.log10(x)) + 1
    #     mask = 10 ** (num_digits - 1)
    #     res = 0
    #     while s > 9:
    #         h = int(s / mask)
    #         l = x % 10
    #         res += h + l * 10 ** mask
    #         s %= mask
    #         s /= 10
    #         mask /= 100
    #     res += s * 10 ** mask
    #     return res * sign

    def reverse(s, x):
        if x == 0: return x
        s = abs(x)
        mod = s % math.pow(2,31)
        if mod != s: return 0
        sign = 1 if x > 0 else -1
        tail = s % 10
        res = 0
        new_res = s // 10
        if new_res * 10 + tail != s: return 0

        n_d = math.floor(math.log10(s))
        while n_d + 1:
            res += tail * 10 ** n_d
            tail = new_res % 10
            new_res //= 10
            n_d -= 1
        if res % math.pow(2, 31) != res: return 0
        return sign * res

so = Solution()
x = -8454654544554
res = so.reverse(x)
print(res)
print(math.pow(2,31))