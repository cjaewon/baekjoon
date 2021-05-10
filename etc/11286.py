minus = []
plus = []

def binarysearch_insert(arr, x):
  start = 0
  end = len(arr) - 1
  mid = 0

  if len(arr) == 0:
    arr.append(x)
    return

  if len(arr) == 1:
    if x < arr[0]:
      arr.insert(0, x)
    else:
      arr.append(x)
    return

  while start <= end:
    mid = (start + end) // 2

    if x < arr[mid]:
      end = mid - 1
    elif x > arr[mid]:
      start = mid + 1
    else: # x == arr[mid]
      break
  
  if x < arr[mid]:
    arr.insert(mid, x)   
  else:
    arr.insert(mid + 1, x)   

for i in range(int(input())):
  x = int(input())

  if x == 0 and len(minus) == 0 and len(plus) == 0:
    print(0)
    continue

  if x == 0 and len(minus) > 0 and len(plus) > 0:
    if minus[0] < plus[0]:
      print("-" + str(minus[0]))
      minus.pop(0)
    elif minus[0] > plus[0]:
      print(plus[0])
      plus.pop(0)
    else:
      print("-" + str(minus[0]))
      minus.pop(0)
  else:
    if x == 0 and len(minus) == 0 and len(plus) > 0:
      print(plus[0])
      plus.pop(0)
    elif x == 0 and len(plus) == 0 and len(minus) > 0:
      print("-" + str(minus[0]))
      minus.pop(0)
    elif x > 0: # plus
      binarysearch_insert(plus, abs(x))
    else: # minus
      binarysearch_insert(minus, abs(x))