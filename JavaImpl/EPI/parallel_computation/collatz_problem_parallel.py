import concurrent.futures
from concurrent import futures

NThreads = 5
RANGESIZE = 10
# Perform basic unit of work
def worker(lower, upper):
    for i in range(lower, upper + 1):
        assert collatz_check(i, set())
    print('(%d, %d)' % (lower, upper))

# Checks an individual number
def collatz_check(x, visited):
    if x == 1:
        return True
    elif x in visited:
        return False
    visited.add(x)
    if x & 1: # odd number
        return collatz_check(3 * x + 1, visited)
    else:
        return collatz_check(x >> 1, visited) # divided by 2

# uses the library thread pool for task assignment and load balancing
executor = futures.ProcessPoolExecutor(max_workers = NThreads)
with executor:
    for i in range(100 // RANGESIZE):
        executor.submit(worker, i * RANGESIZE + 1, (i + 1) * RANGESIZE)


