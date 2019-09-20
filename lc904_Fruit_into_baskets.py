class Solution:
    def totalFruit(self, tree):
        types = {}
        i = j = 0
        max_fruits = 0
        while j < len(tree):
            if len(types) < 2 or tree[j] in types:
                types[tree[j]] = j  # record the most recent index where this character appears
            else:
                max_fruits = max(max_fruits, j - i)  # 3-1 = 2
                # update i: find the other characters last appearance
                to_remain = tree[j - 1]  # 0, 3
                for item in types.keys():
                    if item != to_remain:
                        i = types[item] + 1  # 1, 2
                        del types[item]
                        break
                types[tree[j]] = j  # tree = {0:1, 3:2}, {3:2, 4:3}
            j += 1
        max_fruits = max(max_fruits, j - i)
        return max_fruits




arr = [1,0,3,4,3]
sol = Solution()
res = sol.totalFruit(arr)
print(res)