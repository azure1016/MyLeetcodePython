from collections import Counter
from heapq import *


class Solution:
    def leastInterval(self, tasks, n):
        tasks_counter = Counter(tasks)
        pq = [[-val, key] for key, val in tasks_counter.items()]
        heapify(pq)
        m = 0
        while len(pq) >= 0:
            temp = []
            cycle = n + 1
            while cycle and len(pq):
                cur = heappop(pq)
                cur[0] += 1
                m += 1
                cycle -= 1
                if cur[0] < 0:
                    temp.append([cur[0], cur[1]])
            if len(temp) == 0 and len(pq) == 0:
                return m
            m += cycle
            for task in temp:
                heappush(pq, task)
        return m


tasks = ["A", "A", "A", "B", "B", "B", "B", "C"]
n = 0
res = Solution().leastInterval(tasks, n)
print(res)
