

#implementation of max heap with array
def insert(arr, val):
  size = len(arr)
  arr.append(val)
  # compare it with its parent node: size/2
  current = size
  parent = int((current + 1) / 2) - 1
  while parent >= 0 and arr[parent] < arr[current]:
    arr[parent], arr[current] = arr[current], arr[parent]
    current = parent
    parent = int((current + 1) / 2) - 1
  return arr


def delete(arr):
  size = len(arr)
  arr[0] = arr[size - 1]
  del arr[size - 1]
  size -= 1
  # arr[size] should be filled with some value
  # compare arr[0] with its child and swap with its larger child
  child1, child2 = 1, 2
  parent = 0
  while child2 < size or child1 < size:  # after deletion, the heap size is "size - 1"!
    if child2 < size:
      max_ = max(arr[parent], arr[child1], arr[child2])
      if max_ == arr[parent]:
        break
      elif max_ == arr[child1]:
        arr[child1], arr[parent] = arr[parent], arr[child1]
        parent = child1
      else:
        arr[child2], arr[parent] = arr[parent], arr[child2]
        parent = child2
      child1 = parent * 2 + 1
      child2 = parent * 2 + 2
    else:
      if arr[parent] <= arr[child1]:
        arr[parent], arr[child1] = arr[child1], arr[parent]
      # you can actually break the loop here
      break

  return arr

arr = [1,4,5,3,6,2,8]
heap = []
for i in range(len(arr)):
  insert(heap, arr[i])
print(heap)

delete(heap)
print(heap)
delete(heap)
print(heap)
