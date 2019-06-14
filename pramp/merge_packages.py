#using sort means the algorithm is at least nlogn
def get_indices_of_item_wights(arr, limit):
  dict = {}
  for i in range(len(arr)):
    dict[i] = arr[i]
  print(dict)
  arr.sort()
  #nlogn better than n^2
  i, j = 0, len(arr) - 1
  while i < j:
    current_sum = arr[i] + arr[j]
    if current_sum == limit:break
    elif current_sum > limit:
      j -= 1
    else:
      i += 1
  if arr[i] + arr[j] != limit:
    return []
  result = []
  for key, val in dict.items(): # return the values of the original array:
    if val == arr[i] and key not in result:
      result.append(key)
      del dict[key]
    if val == arr[j] and key not in result:
      result.append(key)
      del dict[key]
  result.sort(reverse = True)
  return result

def get_indices_of_item_weights(arr, limit):
    dict, result = {}, []
    for i in range(len(arr)):
        if arr[i] in dict.values() or limit - arr[i] in dict.values():
            result.append(i)
        dict[i] = arr[i]
#arr = [4, 6, 10, 15, 16]
arr = [4,4,1]
limit = 5
print(get_indices_of_item_wights(arr, limit))