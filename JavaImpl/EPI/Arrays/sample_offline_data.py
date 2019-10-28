'''
uniform random
given [0, n-1] uniform generator

1. sample offline data
n items, k
important: replacement sampling, non-replacement sampling
bernolli trial: non-replacement sampling, either 0 or 1, distribution: hypergeometric distribution
uniform distribution
replacement sampling: [0,1,3,4] first: 2

len(array) == n
[0:k] store chosen number
how to generate the first number:
random from [0:n]: p; swap arr[p], arr[0]
from [1:n], q, swap arr[q], arr[1]
2 / n probability, proof: induction

2. compute a random subset
3. sample online data
4. compute a random permutation
5. generate non-uniform random numbers
'''
from random import *
def sample_offline_data(arr, k):
    for i in range(k):
        p = randint(i, n-1) # inclusive
        arr[i], arr[p] = arr[p], arr[i]
    return arr[:k]
