from collections import Counter
class Dominos:
    def rotate_3(self, A, B):
        counterA = [0 for _ in range(7)]
        counterB = [0 for _ in range(7)]
        intersection = [0 for _ in range(7)]
        for i in range(len(A)):
            counterA[A[i]] += 1
            counterB[B[i]] += 1
            if A[i] == B[i]:
                intersection[A[i]] += 1

        for i in range(1, 7):
            if counterA[i] + counterB[i] - intersection[i] >= len(A):
                return min(counterA[i], counterB[i]) - intersection[i]
        return -1
    # beat 50%
    def rotate_1(self, A, B):
        counter_a = Counter(A)
        counter_b = Counter(B)
        pivot_a = counter_a.most_common()[0]
        pivot_b = counter_b.most_common()[0]
        steps = 0
        if pivot_a[1] > pivot_b[1]:
            steps = self.flip(A, B, pivot_a[0])
        else:
            steps = self.flip(B, A, pivot_b[0])
        return steps
    # beat 60%
    def rotate_2(self, A, B):
        n = len(A)
        a, b = 0, 0
        for i in range(n):
            if A[i] == A[0] or B[i] == A[0]:
                if A[i] != A[0]: a += 1
                elif B[i] != A[0]: b += 1
                if i == n - 1: return min(a, b)
            else: break
        
        a, b = 0, 0
        for i in range(n):
            if A[i] == B[0] or B[i] == B[0]:
                if A[i] != B[0]: a += 1
                elif B[i] != B[0]: b += 1
                if i == n - 1: return min(a, b)
            else: return -1
            
            

    def flip(self, A, B, pivot):
        steps = 0
        for a, b in zip(A, B):
            if a == pivot:
                continue
            elif b == pivot:
                steps += 1
            else: return -1
        return steps

    def test1(self):
        A = [2, 1, 2, 4, 2, 2]
        B = [5, 2, 6, 2, 3, 2]
        res = self.rotate(A, B)
        print(res == 2)

    def test2(self):
        A = [3, 5, 1, 2, 3]
        B = [3, 6, 3, 3, 4]
        res = self.rotate(A, B)
        print(res == -1)

    def test3(self):
        A = [2, 3, 3, 3, 3, 2, 2, 2]
        B = [3, 2, 2, 2, 2, 3, 3, 3]
        print(self.rotate(A, B) == 4)
    
    


sol = Dominos()
sol.test2()
sol.test1()
sol.test3()



