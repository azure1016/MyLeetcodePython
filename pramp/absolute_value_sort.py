from Queue import PriorityQueue

# in-place quick sort
def absSort(arr):
    my_quick_sort(arr)
    return arr

def my_quick_sort(arr, pivot):
    p = partition(arr, pivot)
    my_quick_sort(arr[:p], p // 2)
    my_quick_sort(arr[p:], (len(arr) - p) // 2)

def partition(arr, pivot):
    arr[pivot], arr[-1] = arr[-1], arr[pivot]

# in-place max heap sort
def absSort4(arr):
    for i in range(1, len(arr)):
        put(arr, i)
    for i in reversed(range(len(arr))):
        get(arr, i)
    return arr

def compare(a, b):
    if abs(a) > abs(b): return True
    elif abs(a) < abs(b): return False
    return a > b
def put(arr, cur_heapsize):
    '''
    :param arr: current heap
    :param cur_heapsize: the size of heap before putting the new element, or the index to insert new element
    :return:
    '''
    while cur_heapsize > 0:
        parent = (cur_heapsize - 1) // 2
        if compare(arr[cur_heapsize], arr[parent]):
            arr[cur_heapsize], arr[parent] = arr[parent], arr[cur_heapsize]
            cur_heapsize = parent
        else: break

def get(arr, where_to_store, index = 0):
    '''
    :param arr:
    :param where_to_store:where to put the top element
    :param index:
    :return:
    '''
    arr[index], arr[where_to_store] = arr[where_to_store], arr[index]
    parent = index
    while parent <= (where_to_store - 2) // 2:
        child1, child2 = 2 * parent + 1, 2 * parent + 2
        if child1 == where_to_store - 1:
            if compare(arr[child1], arr[parent]):
                arr[parent], arr[child1] = arr[child1], arr[parent]
            break
        if compare(arr[child1], arr[child2]):
            arr[parent], arr[child1] = arr[child1], arr[parent]
            parent = child1
        else:
            arr[parent], arr[child2] = arr[child2], arr[parent]
            parent = child2



#in-place bubble sort
def absSort3(arr):
    for i in reversed(range(len(arr))):
        for j in range(i):
            if abs(arr[j]) > abs(arr[j+1]) or (abs(arr[j]) == abs(arr[j+1]) and arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# absolute value sort using priority queue: implementation 2
def absSort2(arr):
    res = []
    minHeap = PriorityQueue()

# absolute value sort using priority queue: implementation 1
def absSort1(arr):
    negative = PriorityQueue()  # m negative , l positive , n == m + l
    positive = PriorityQueue()
    for num in arr:
        if num < 0:
            negative.put(-num)
        else:
            positive.put(num)
    # merge these two arrays:
    merged = []
    if negative.qsize() > 0:
        top_neg = negative.get()  # negative is empty
    else: top_neg = None
    if positive.qsize() > 0:
        top_pos = positive.get()
    else: top_pos = None
    while top_neg is not None and top_pos is not None:
        # the top element in a min heap
        if top_neg <= top_pos:
            merged.append(-top_neg)
            if negative.qsize() > 0:
                top_neg = negative.get()
            else: top_neg = None
        else:
            merged.append(top_pos)
            if positive.qsize() > 0:
                top_pos = positive.get()
            else: top_pos = None
    if top_neg is not None:
        merged.append(-top_neg)
    if top_pos is not None:
        merged.append(top_pos)
    while negative.qsize() > 0:  # there are remained elements in negative
        merged.append(-negative.get())
    while positive.qsize() > 0:
        merged.append(positive.get())

    return merged

arr = [2, -7, 5, -2, -2, 0]
res = absSort(arr)
print(res)

# scan the array, slit the array into negative numbers, positives numbers, sort them using heap sort; merge these two arrays using merge sort
