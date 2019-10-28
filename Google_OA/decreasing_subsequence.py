class Sequence:
    def genSubsequence(self, nums):
        piles = []
        for i, num in enumerate(nums):
            is_piled = False
            for pile in piles:
                if pile[-1] > num:
                    pile.append(num)
                    is_piled = True
                    break
            if not is_piled:
                piles.append([num])
        return piles

    def minDecreasingSubsequence(self, nums):
        piles = self.genSubsequence(nums)
        return len(piles)
    
    def test(self, arr):
        print(self.genSubsequence(arr))

sol = Sequence()
arr1 = [5,2,4,3,1,6]
sol.test(arr1)
print("----------------")
arr2 = [2,9,12,13,4,7,6,5,10]
sol.test(arr2)

print("--------")
arr3 = [1,1,1]
sol.test(arr3)
            