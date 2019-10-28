# EPI 5.10 permute the elements of an array
def permute(perm, A):
    '''
    A is the collections of chars
    perm is the instruction for permutations
    '''
    n = len(perm)
    for i in range(n):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= n
            next = temp
    return A 

def permute_n_square(perm, A):
    # permute in space O(1) without modifying perm; but O(n^2) time
    def permute(perm, A, start):
        i, temp = start, A[start]
        while True:
            temp = A[perm[i]]
            A[i], A[perm[i]] = A[perm[i]], A[i] # A[start], A[perm[start]] = A[perm[start]], A[start]
            i = perm[i]
            
def test(perm, A):
    result = permute(perm, A)
    print(result)

perm = [2,0,1,3]
A = ['a', 'b', 'c', 'd']
test(perm, A)  # expected: b,c,a,d   

perm2 = [3,2,1,0]
A2 = ['a', 'b', 'c', 'd']
test(perm2, A2) # expected: d, c, b, a

            