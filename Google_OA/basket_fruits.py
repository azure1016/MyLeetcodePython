class Picker:
    def totalFruit(self, trees):
        '''
        cur: current node
        last: the last different node adjacent to the current node
        total: the local total fruits we can pick within 2 categories of fruits
        max_fruits: the global maximum fruits we can pick of 2 categories
        '''
        cur, last = None, None
        total = 0
        max_fruits = 0
        count_cur = count_last = 0
        for i, tree in enumerate(trees):
            if cur is None or tree == cur:
                cur = tree
                count_cur += 1
            else:
                total += count_cur
                if tree != last and tree != cur:
                    max_fruits = max(max_fruits, total)
                    total = count_cur
                last, cur = cur, tree
                count_last = count_cur
                count_cur = 1
        return max(max_fruits, total+count_cur)

    def test(self):
        arr = [0, 1, 2, 2]
        res = self.totalFruit(arr)
        print(res)

sol = Picker()
sol.test()


