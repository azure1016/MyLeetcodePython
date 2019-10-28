class Solution:
    def hIndex(self, citations):
        '''
        [0,1,3,5,6]
        first thought: sort it then do a binary search, nlogn
        but count sort would be better
        ''' 
        n = len(citations)
        bucket = [0] * (n + 1)
        for i, cite in enumerate(citations):
            if cite >= n:
                bucket[n] += 1
            else:
                bucket[cite] += 1
        
        count = 0
        for i in reversed(range(n+1)):
            count += bucket[i]
            if count >= i: return i
        return 0

citations = [0, 0]
h = Solution().hIndex(citations)
print(h)