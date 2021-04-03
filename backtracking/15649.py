n, m = map(int, input().split(" "))

arr = [0 for i in range(10)]
used = [0 for i in range(10)]

def back(k):
  if k == m:
    for i in range(m):
      print(arr[i], end=" ")
    print()
    return
  for i in range(1, n + 1):
    if used[i] == 1:
      continue
    arr[k] = i
    used[i] = 1
    back(k + 1)
    used[i] = 0

back(0)