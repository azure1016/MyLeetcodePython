# return the largest subarray with length of K in an array
# A is larger than B if for the first unmatched elements in A is bigger than that in B

class LargerArray:
    # elements in A are unique
    def largest_array(self, A, k):
        start = 0
        for i in range(len(A) - k + 1):
            if A[i] > A[start]:
                start = i
        return A[start: start+k]

    # elements in A are not unique
    def largest_array_dup(self, A, k):
        start = 0
        for i in range(len(A) - k + 1):
            if self.compare(A[i:i+k], A[start:start+k]):
                start = i
        return A[start: start + k]

    def compare(self, a, b):
        for x, y in zip(a, b):
            if x > y: return True
            elif x < y: return False
        return True


sol = LargerArray()
arr_unique = [1,4,2,6,5,3]
res_unique = sol.largest_array(arr_unique, 3)
print(res_unique)

arr_dup = [1,2,2,2,2,6,5]
res_dup = sol.largest_array_dup(arr_dup, 3)
print(res_dup)

