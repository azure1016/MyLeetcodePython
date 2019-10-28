class Jumper:
    def oddEvenJump(self, jumps):
        next_higher, next_lower = self.logSetup(jumps)
        higher = [False] * len(jumps) # the good starting index as odd-numbered jumps
        lower = [False] * len(jumps) # the good starting index as even-numbered jumps
        higher[-1] = lower[-1] = True
        for i in reversed(range(len(jumps) - 1)):
            higher[i] = lower[next_higher[i]] # next_higher[i] will return an index from where we would do an even-numbered jump
            lower[i] = higher[next_lower[i]]
        return sum(higher)

    # O(nlogn)
    def logSetup(self, jumps):
        next_higher, next_lower = [0] * len(jumps), [0] * len(jumps)
        monotone_stack = []
        for _, i in sorted((a, i) for i, a in enumerate(jumps)):
            while monotone_stack and monotone_stack[-1] < i:
                next_higher[monotone_stack.pop()] = i
            monotone_stack.append(i)

        monotone_stack = []
        for _, i in sorted((-a, i) for i, a in enumerate(jumps)):
            while monotone_stack and monotone_stack[-1] < i:
                next_lower[monotone_stack.pop()] = i
            monotone_stack.append(i)
        return next_higher, next_lower


    # O(n^2)
    def setup(self, jumps):
        '''
        :param jumps:
        :return: 2 arrays: the next higher, and the next lower
        '''
        next_higher, next_lower = [0] * len(jumps), [0] * len(jumps)

        for i, val in enumerate(jumps):
            try:
                sorted_tp = [(v, idx) for idx, v in enumerate(jumps[i+1:], i+1) if v >= val]
                sorted_tp.sort()
                next_higher[i] = sorted_tp[0][1]
            except:
                next_higher[i] = 0
            try:
                sorted_tp = [(v, len(jumps) - idx) for idx, v in enumerate(jumps[i+1:], i+1) if v <= val]
                sorted_tp.sort()
                next_lower[i] = len(jumps) - sorted_tp[-1][1]
            except:
                next_lower[i] = 0
        return next_higher, next_lower

    def test1(self):
        jumps = [10,13,12,14,15]
        print(self.oddEvenJump(jumps))

    def test2(self):
        jumps = [2,3,1,1,4]
        print(self.oddEvenJump(jumps))

sol = Jumper()
sol.test1()
sol.test2()