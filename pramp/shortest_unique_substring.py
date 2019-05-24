def get_shortest_unique_substring_mine(arr, str):
    if len(str) < len(arr): return ""
    frequency = {}
    for char in arr:
        frequency[char] = 0

    i, j = 0, len(arr) - 1
    min_len, res = len(str), None
    for char in str[i: j + 1]:
        if char in arr:
            frequency[char] += 1
    if min(frequency.values()) >= 1: return str[i:j + 1]
    #while i <= j + 1 - len(arr) and j + 1 < len(str):
    while i <= j + 1 -len(arr):
        while j + 1 < len(str) and min(frequency.values()) < 1:
            j += 1
            if str[j] in arr:
                frequency[str[j]] += 1
        # while i <= j + 1 - len(arr) and min(frequency.values() > 0):
        while min(frequency.values()) > 0:
            if str[i] in arr:
                if frequency[str[i]] > 1:
                    frequency[str[i]] = frequency[str[i]] - 1
                    i += 1
                else:
                    break
            else:
                i += 1
        if min(frequency.values()) > 0:
            if j - i + 1 <= min_len:
                res = (i, j)
                min_len = j - i + 1
            frequency[str[i]] = frequency[str[i]] - 1
        i += 1
    if res != None:
        minSubStr = str[res[0]:res[1] + 1]
        return minSubStr
    else:
        return ""

#Bubu's solution
import collections
def get_shortest_unique_substring(s, t):
    need, missing = collections.Counter(t), len(t)
    left = I = J = 0
    for right, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if J == 0 or right - left <= J - I:
                I, J = left, right
    return s[I:J]

def minWindow(t, s):
    if len(t) > len(s):return ""
    left = I = J = 0
    need, missing = collections.Counter(t), len(t)
    for idx, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1
        if missing == 1:
            right = idx
            while left < right and missing == 0:
                missing += need[str[left]] == 0
                need[str[left]] += 1
                left += 1
            if J == 0 or right - left + 1 <= J - I:
                I = left - 1
                J = right
    return str[I:J]

#result = get_shortest_unique_substring(["A","B","C","E","K","I"], "KADOBECODEBANCDDDEI")
result = minWindow("ABC", "KADOBECODEBANCDDDEI")
print(result)

#use max heap to solve the question