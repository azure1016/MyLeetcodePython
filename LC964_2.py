import sys

class Solution:
    def __init__(self):
        self.rec = {}
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """

        if target == 1:
             return 1
        if x == 2:
            self.rec[2] = 0
        if target in self.rec:
            return self.rec.get(target)
        else:
            opt1, opt2 = sys.maxsize, sys.maxsize
            tmp = x
            count = 0
            while tmp < target:
                tmp = tmp * x
                count = count + 1
            if tmp == target:
                #self.rec[target] = count
                opt1 = count
                #return count
            else:
                if tmp - target < target:
                    iTar = tmp - target
                    opt1 = count + 1 + self.leastOpsExpressTarget(x, iTar)
            tmp = int(tmp / x)
            if count > 0:
                count = count - 1
            if count == 0 and tmp == 1:
                count = 1
            iTar_2 = target - tmp
            opt2 = count + 1 + self.leastOpsExpressTarget(x, iTar_2)#count = count - 1 + 1 + least(x, target - tmp)
            ans = min(opt1, opt2)
            self.rec[target] = ans
            return ans

if __name__ == "__main__":
    ins = Solution()
    print(ins.leastOpsExpressTarget(3,929))