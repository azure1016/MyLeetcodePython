'''
The set {0,1.,2,… ,n - 1} has n!/((n - k)!/k!) subsets of size k. We seek to design an algorithm that returns any one of these subsets with equal probability.
Write a program that takes as input a positive integer n and a size k < n, and returns a size-k subset of {0,1,…,n-1}. The subset should be represented as an array. All subsets should be equally likely and, in addition, all permutations of elements of the array should be equally likely.

len(arr) = n, arr[i] = i: imagination
hashtable{(0, 2), (1, 1), (2, 0) ,(3, 7)| (7, 3) }
[0,1,2,3,4, 5, 6, 7,8, 9,10]
1st: 2, swap arr[0], arr[2], i = 0
2nd: 1, swap arr[1], arr[1], i = 1
3rd: 2, swap arr[2], with arr[2], i = 2 (2, 2) not in hashtable
4st: 7, swap arr[3] with arr[7], i = 3,
5st:7, (4, 3); non-replace
6st: 8
for i in range(k):
    hashtable[i] -- [2,1,0,7] subset
'''
import random
# from random import *
def random_subset(n, k):
    changed_items = {}
    for i in range(k):
        # find an index to store the element at that location
        rand_idx = random.randint(i, n-1) # 1-n
        stored_at_rand_idx = changed_items.get(rand_idx, rand_idx)
        mapped_i = changed_items.get(mapped_i, mapped_i)
        changed_items[i] = stored_at_rand_idx
        change_items[rand_idx] = mapped_i
    return [changed_items[key] for key in range(k)] # list comprehension


