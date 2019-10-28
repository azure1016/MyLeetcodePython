import collections
import string

# uses BFS to find the least steps of tranformations
def transform_string(D, s, t):
    StringWithDistance = collections.namedtuple('StringWithDistance', 'candidate_string, distance')
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s) # Marks s as visited by erasing it in D. 
    # What if s is not necessarily in D?

    while q:
        f = q.popleft()
        if f.candidate_string == t: return f.distance
    # Tries all possible transformations of f.candidate_string
        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase: # Iterates through 'a' ~ 'z'
                cand = f.candidate_string[:i] + c + f.candidate_string[i+1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))
    return -1 # cannnot find a possible transformation


s = 'cat'
t = 'dog'
D = set(['bat', 'dot', 'cot', 'dog', 'dag', 'cat'])
res = transform_string(D, s, t)
print(res == 3)
