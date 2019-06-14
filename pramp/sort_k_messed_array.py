#working, but too slow
def sort_k_messed_array_original(arr, k):
  if not arr: return arr
  i = 0
  res = []
  step = 2 * k #k = 2, step = 5
  while i + step < len(arr): #[0,1) i = 0
    arr[i: i+step] = sorted(arr[i : i + step]) # arr[0:5] = arr[0, 1,2,3,4]
    i = i + k
  if i < len(arr):
    arr[i:] = sorted(arr[i:])
  return arr


def alternate_using_min_heap(arr, k):
    #initialize the 2*k min heap
    size = len(arr)
    for i in range(2 * k):
        insert(arr, i)
    for i in range(2 * k, size):
        delete(arr, 2 * k, i)
        #insert(arr, 2 * k, i + 1)
    arr[:2 * k] = sorted(arr[:2 * k])
    for i in range(2 * k):
        arr.append(arr[i])
    for i in range(2 * k):
        del arr[0]
    return arr


def delete(arr, n, pos):
    arr[0], arr[pos] = arr[pos], arr[0]
    parent, child1, child2 = 0, 1, 2
    while child2 < n or child1 < n:
        if child2 < n:
            min_ = min(arr[parent], arr[child1], arr[child2])
            if min_ == arr[parent]:break
            elif min_ == arr[child1]:
                arr[child1], arr[parent] = arr[parent], arr[child1]
                parent = child1
            else:
                arr[child2], arr[parent] = arr[parent], arr[child2]
                parent = child2
            child1 = parent * 2 + 1
            child2 = parent * 2 + 2
        else:
            if arr[parent] > arr[child1]:
                arr[parent],arr[child1] = arr[child1], arr[parent]
            break

def insert(arr, pos):
    current = pos
    parent = int((current - 1) / 2)
    while parent >= 0 and arr[current] < arr[parent]:
        arr[current], arr[parent] = arr[parent], arr[current]
        current = parent
        parent = int((current - 1) / 2)



arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
#result = sort_k_messed_array_original(arr, k)
result = alternate_using_min_heap(arr, k)
print(result)