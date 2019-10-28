class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        '''
        space O(1)
        time O(n)
        easier than DP
        '''
        n = len(nums)
        w1, w2, w3 = sum(nums[i] for i in range(k)), sum(nums[i] for i in range(k, 2*k)), sum(nums[i] for i in range(2*k, 3*k))
        mw1, mw2, mw3 = w1, w1+w2, w1+w2+w3 # prefix sum
        mw1Index, mw2Index, mw3Index = [0], [0, k], [0, k, 2*k] # mw1, mw2, mw3's index
        for i in range(1, n - 3*k + 1): # starting index for w1 will be at most n-3k
            w1 += nums[i + k - 1] - nums[i - 1] 
            w2 += nums[i + 2*k - 1] - nums[i + k - 1]
            w3 += nums[i + 3*k - 1] - nums[i + 2*k - 1]
            if w1 > mw1:
                mw1 = w1
                mw1Index = [i]
            if w2+mw1 > mw2:
                mw2 = w2+mw1
                mw2Index = mw1Index + [i+k]
            if w3+mw2 > mw3:
                mw3 = w3 + mw2
                mw3Index = mw2Index + [i + 2*k]
        return mw3Index
    
    def maxSumOfThreeSubarrays_2(self,nums, k):
        n=len(nums)
        w1,w2,w3=sum(nums[i] for i in range(k)),sum(nums[i] for i in range(k,2*k)),sum(nums[i] for i in range(2*k,3*k))
        mw1,mw2,mw3=w1,w1+w2,w1+w2+w3
        mw1index,mw2index,mw3index=[0],[0,k],[0,k,2*k]#mw1,mw2,mw3's index.
        for i in range(1,n-3*k+1):#last index for w1 window will be n-3k
            w1+=nums[i-1+k]-nums[i-1]
            w2+=nums[i-1+2*k]-nums[i-1+k]
            w3+=nums[i-1+3*k]-nums[i-1+2*k]
            if w1>mw1:
                mw1,mw1index=w1,[i]
            if mw1+w2>mw2:
                mw2,mw2index=mw1+w2,mw1index+[i+k]
            if mw2+w3>mw3:
                mw3,mw3index=mw2+w3,mw2index+[i+2*k]
        return mw3index
    def test(self, nums, k):
        result = self.maxSumOfThreeSubarrays(nums, k)
        print("result:", result)
        print("values:", [nums[i] for i in result])

so = Solution()
nums1 = [4,3,8,5,2,9,5,0,5,2,4,8,7,1,9,5,3]
k1 = 3
nums2 = [1,2,1,2,6,7,5,1]
k2 = 2
so.test(nums1, k1)
so.test(nums2, k2)
