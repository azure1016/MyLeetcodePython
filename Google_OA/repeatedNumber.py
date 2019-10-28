def repeatedNumber(arr):
    for i in arr:
        if arr[abs(i)-1] > 0:
            arr[abs(i)-1] = -arr[abs(i)-1]
        else: return abs(i)

def test(arr):
    print(repeatedNumber(arr))

def rpN(arr):
    for i in range(len(arr)):
	      if arr[arr[i]-1] != arr[i]:
		        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]

  # scan again
    for i in range(len(arr)):
	      if arr[i] != i + 1:
		        return arr[i]
def test1(arr):
    print(rpN(arr))

arr = [7,6,4,4,3,2,1]
arr2 = [3,4,5,2,1,2]
test(arr)
test1(arr2)

  