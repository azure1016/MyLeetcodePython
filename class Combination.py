import sys
import unittest
class Combination:
    def __init__(self):
        pass

    def largestCombination(self, A, B, target):
        cur_max = [(-1, -1, -sys.maxsize)] # record the index of elements from A and B
        sorted_A = sorted((a[1], a[0]) for a in A)
        sorted_B = sorted((b[1], b[0]) for b in B)
        i, j = 0, len(B) - 1
        while i < len(A) and j >= 0:
            sum2 = sorted_A[i][0] + sorted_B[j][0]
            if sum2 > target: 
                j -= 1
                continue
            if sum2 > cur_max[0][2]: 
                cur_max = [(sorted_A[i][1], sorted_B[j][1], sum2)]
                i += 1
            elif sum2 == cur_max[0][2]: 
                cur_max.append((sorted_A[i][1], sorted_B[j][1], sum2))
                runner = j
                while runner >= 0 and sorted_B[runner] == sorted_B[runner-1]:
                    cur_max.append((sorted_A[i][1], sorted_B[runner][1], sum2))
                i += 1

        if cur_max[0][0] != -1:
            return [[a,b] for (a, b, _) in cur_max if a != -1]
        return []

class MyTest(unittest.TestCase):
    def __init__(self, args):
        super(MyTest, self).__init__(args)

    def test1(self):
        a = [[1, 3], [2, 5], [3, 7], [4, 10]]
        b = [[1, 2], [2, 3], [3, 4], [4, 5]]
        target = 10
        solver = Combination()
        res = solver.largestCombination(a, b, target)
        print(res)
        len_res = len(res)
        self.assertEquals(len_res, 2)
        self.assertIn([2,4], res, "[2,4]")
        self.assertIn([3,2], res, "[3,2]")

    def test2(self):
        a = [[1, 2], [2, 4], [3, 6]]
        b = [[1, 2]]
        target = 7
        solver = Combination()
        res = solver.largestCombination(a, b, target)
        print(res)
        len_res = len(res)
        self.assertEquals(len_res, 1)
        self.assertIn([2,1], res, "[2,4]")


    def test3(self):
        a = [[1, 8], [2, 7], [3, 14]]
        b = [[1, 5], [2, 10], [3, 14]]
        target = 20
        solver = Combination()
        res = solver.largestCombination(a, b, target)
        print(res)
        len_res = len(res)
        self.assertEquals(len_res, 1)
        self.assertIn([3, 1], res, "[3,1]")

    def test4(self):
        a = [[1, 8], [2, 15], [3, 9]]
        b = [[1, 8], [2, 11], [3, 12]]
        target = 20
        solver = Combination()
        res = solver.largestCombination(a, b, target)
        print(res)
        len_res = len(res)
        self.assertEquals(len_res, 2)
        self.assertIn([1, 3], res)
        self.assertIn([3, 2], res)



test = MyTest('test1')
test.test1()
test.test2()
test.test3()
test.test4()





