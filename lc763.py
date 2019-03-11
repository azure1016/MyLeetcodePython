class Solution:
    # def partitionLabels(self, S: str) -> List[int]:
    #     seen = {}
    #     breakpts = []
    #     for i in range(len(arr)):
    #         if not arr[i] in seen:
    #             seen[arr[i]] = i
    #             breakpts.append(i)
    #     else:#arr[i] = 1
    #         for j in range(seen[arr[i]], i):
    #             if j in breakpts:
    #                 seen[arr[j]] = i
    #                 breakpts.remove(j)
    #            seen[arr[i]] = j
    #         breakpts.append(i)
    #         seen[arr[i]] = i

    # res = []
    # res.append(breakpts[0]+1)
    # #[9,12,23]
    # for i in range(1, len(breakpts)):
    #     res.append(breakpts[i]-breakpts[i-1])
    # return res
    def partitionLabels(self, arr):
        '''
        ababcbacadefegdehijhklij
        012345678901234567890123
                 ^
        a,b,c
        qiejxqfnqceocmy
        012345678901234
                   ^
        '''
        last_i, i, j = -1, 0, 0
        n = len(arr)
        res = []
        while i < n:
            occurred_chars = [arr[i]]
            j = i + 1
            while j < n:
                if arr[j] in occurred_chars:
                    occurred_chars = list(set(occurred_chars + list(arr[i:j])))
                    i = j #update the slower ptr
                j += 1
            res.append(i - last_i)
            last_i = i
            i += 1 #you have to move i, or else the while loop will never end?
        return res

p = Solution()
res = p.partitionLabels("ababcbacadefegdehijhklij")
print(res)